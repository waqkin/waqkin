import EmptyState from "@/components/EmptyState";

export default function Turkcell() {
  return (
    <EmptyState
      icon="📶"
      title="Turkcell hattı bağlı değil"
      description="Kalan kullanım ve fatura bilgisi, kendi hesabınla kendi rızanla giriş yapılan bir tarayıcı otomasyonu ile okunacak."
      note="Resmi/genel kullanıma açık bir API bulunmadığından bu entegrasyon kırılgan olabilir ve Turkcell'in arayüz değişiklikleriyle bozulabilir."
    />
  );
}
