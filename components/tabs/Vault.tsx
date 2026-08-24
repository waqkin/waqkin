import EmptyState from "@/components/EmptyState";

export default function Vault() {
  return (
    <EmptyState
      icon="🗝️"
      title="Kasa bağlı değil"
      description="Parola ve hesap bilgileri, self-host edilen Vaultwarden sunucusu üzerinden uçtan uca şifrelenmiş şekilde yönetilecek."
      note="Ana parola hiçbir zaman sunucuya gönderilmez; tüm şifre çözme işlemleri istemci tarafında yapılır."
    />
  );
}
