import EmptyState from "@/components/EmptyState";

export default function Subscriptions() {
  return (
    <EmptyState
      icon="🔁"
      title="Henüz tespit edilen abonelik yok"
      description="Banka/kredi kartı işlem geçmişindeki işlem açıklamaları taranarak Netflix, Spotify gibi tekrarlayan ödemeler otomatik olarak kategorilendirilecek."
      note="Bu sekme, banka hesapları bağlandıktan sonra otomatik olarak dolmaya başlar."
    />
  );
}
