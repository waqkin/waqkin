"use client";

import { FormEvent, useState } from "react";

interface LoginScreenProps {
  onUnlock: () => void;
}

export default function LoginScreen({ onUnlock }: LoginScreenProps) {
  const [masterPassword, setMasterPassword] = useState("");
  const [error, setError] = useState("");

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (masterPassword.trim().length === 0) {
      setError("Ana parola boş olamaz.");
      return;
    }
    // TODO: gerçek client-side türetme/şifre çözme burada yapılacak
    // (ör. Argon2/PBKDF2 ile anahtar türetimi). Şu an sadece panel
    // iskeletini açan bir mock kontrol.
    setError("");
    onUnlock();
  }

  return (
    <main className="flex min-h-screen items-center justify-center bg-[var(--background)] px-4">
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-sm rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-8 shadow-xl"
      >
        <div className="mb-6 text-center">
          <div className="mx-auto mb-3 flex h-12 w-12 items-center justify-center rounded-xl bg-[var(--accent)]/10 text-2xl">
            🔐
          </div>
          <h1 className="text-lg font-semibold text-[var(--foreground)]">
            Finans &amp; Hesap Paneli
          </h1>
          <p className="mt-1 text-sm text-[var(--muted)]">
            Devam etmek için ana parolanı gir
          </p>
        </div>

        <label className="mb-1 block text-xs font-medium text-[var(--muted)]">
          Ana Parola
        </label>
        <input
          type="password"
          autoFocus
          value={masterPassword}
          onChange={(event) => setMasterPassword(event.target.value)}
          placeholder="••••••••••••"
          className="w-full rounded-lg border border-[var(--border)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--foreground)] outline-none focus:border-[var(--accent-2)]"
        />

        {error && (
          <p className="mt-2 text-xs text-[var(--danger)]">{error}</p>
        )}

        <button
          type="submit"
          className="mt-5 w-full rounded-lg bg-[var(--accent)] py-2 text-sm font-medium text-[#06110c] transition hover:opacity-90"
        >
          Kilidi Aç
        </button>

        <p className="mt-4 text-center text-[11px] leading-relaxed text-[var(--muted)]">
          Ana parolan hiçbir zaman sunucuya gönderilmez; tüm şifreleme
          istemci tarafında yapılır.
        </p>
      </form>
    </main>
  );
}
