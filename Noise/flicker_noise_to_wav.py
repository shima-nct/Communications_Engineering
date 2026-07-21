from __future__ import annotations

import argparse
import wave
from pathlib import Path

import numpy as np


def colored_noise_1_over_f(*, alpha: float, n: int, fs: int, seed: int, fmin: float) -> np.ndarray:
    f = np.fft.rfftfreq(n, d=1.0 / fs)

    rng = np.random.default_rng(seed)
    spectrum = rng.normal(size=len(f)) + 1j * rng.normal(size=len(f))

    spectrum[0] = 0.0

    f_eff = np.maximum(f, fmin)
    weights = np.zeros_like(f_eff)
    nonzero = f > 0
    weights[nonzero] = 1.0 / (f_eff[nonzero] ** (alpha / 2.0))

    x = np.fft.irfft(spectrum * weights, n=n)
    x = x - x.mean()
    x = x / (x.std() + 1e-12)
    return x


def write_wav_mono_int16(path: Path, *, x: np.ndarray, fs: int) -> None:
    x = np.asarray(x, dtype=np.float64)

    x = np.tanh(x / 2.0)

    peak = float(np.max(np.abs(x)))
    if peak > 0:
        x = 0.95 * (x / peak)

    pcm = (x * 32767.0).astype(np.int16)

    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(pcm.tobytes())


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate flicker noise (1/f^alpha) and save as WAV.")
    parser.add_argument("--alpha", type=float, default=1.0, help="PSD slope alpha (alpha=1.0 is flicker)")
    parser.add_argument("--seconds", type=float, default=10.0, help="Duration in seconds")
    parser.add_argument("--fs", type=int, default=44_100, help="Sampling rate")
    parser.add_argument("--seed", type=int, default=0, help="RNG seed")
    parser.add_argument("--fmin", type=float, default=20.0, help="Lower bound for 1/f weighting (Hz)")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output WAV path (default: Noise/flicker_noise_alpha*_fs*_T*.wav)",
    )

    args = parser.parse_args()

    n = int(args.fs * args.seconds)
    x = colored_noise_1_over_f(alpha=args.alpha, n=n, fs=args.fs, seed=args.seed, fmin=args.fmin)

    out = args.out
    if out is None:
        out = Path("Noise") / f"flicker_noise_alpha{args.alpha:g}_fs{args.fs}_T{args.seconds:g}.wav"

    write_wav_mono_int16(out, x=x, fs=args.fs)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
