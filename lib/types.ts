export type TabId =
  | "overview"
  | "bank"
  | "turkcell"
  | "turktelekom"
  | "subscriptions"
  | "vault";

export interface TabDefinition {
  id: TabId;
  label: string;
  description: string;
}

export const TABS: TabDefinition[] = [
  {
    id: "overview",
    label: "Genel Bakış",
    description: "Tüm hesapların özet görünümü",
  },
  {
    id: "bank",
    label: "Banka Hesapları",
    description: "Açık Bankacılık ile bağlı hesaplar",
  },
  {
    id: "turkcell",
    label: "Turkcell",
    description: "Hat kullanımı ve fatura bilgisi",
  },
  {
    id: "turktelekom",
    label: "Türk Telekom",
    description: "Hat kullanımı ve fatura bilgisi",
  },
  {
    id: "subscriptions",
    label: "Abonelikler",
    description: "İşlem geçmişinden tespit edilen abonelikler",
  },
  {
    id: "vault",
    label: "Parola / Hesap Kasası",
    description: "Vaultwarden entegrasyonu",
  },
];
