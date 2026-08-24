import EmptyState from "@/components/EmptyState";

export default function BankAccounts() {
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-sm font-medium text-[var(--muted)]">
          Bağlı Banka Hesapları
        </h2>
        <button
          disabled
          className="cursor-not-allowed rounded-lg border border-[var(--border)] px-3 py-1.5 text-xs text-[var(--muted)]"
        >
          + Hesap Bağla
        </button>
      </div>
      <EmptyState
        icon="🏦"
        title="Henüz bağlı banka hesabı yok"
        description="Hesaplar, bankanın resmi Açık Bankacılık (Open Banking) API'si üzerinden OAuth benzeri bir yetkilendirme akışıyla bağlanır."
        note="Ekran kazıma veya otomatik giriş kullanılmaz — sadece resmi ve yasal entegrasyon yöntemleri desteklenir."
      />
    </div>
  );
}
