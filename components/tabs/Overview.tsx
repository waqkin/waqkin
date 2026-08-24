import EmptyState from "@/components/EmptyState";

const SUMMARY_CARDS = [
  { label: "Toplam Bakiye", value: "—", accent: "var(--accent)" },
  { label: "Bu Ay Harcama", value: "—", accent: "var(--accent-2)" },
  { label: "Aktif Abonelik", value: "—", accent: "var(--muted)" },
  { label: "Kalan İnternet", value: "—", accent: "var(--muted)" },
];

export default function Overview() {
  return (
    <div className="space-y-6">
      <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
        {SUMMARY_CARDS.map((card) => (
          <div
            key={card.label}
            className="rounded-xl border border-[var(--border)] bg-[var(--surface)] p-4"
          >
            <p className="text-xs text-[var(--muted)]">{card.label}</p>
            <p
              className="mt-2 text-xl font-semibold"
              style={{ color: card.accent }}
            >
              {card.value}
            </p>
          </div>
        ))}
      </div>

      <EmptyState
        icon="📊"
        title="Henüz veri bağlanmadı"
        description="Banka hesaplarını, operatör hatlarını ve abonelikleri bağladığında genel bakış burada otomatik olarak oluşacak."
      />
    </div>
  );
}
