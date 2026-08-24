import EmptyState from "@/components/EmptyState";

export default function TurkTelekom() {
  return (
    <EmptyState
      icon="📡"
      title="Türk Telekom hattı bağlı değil"
      description="Öncelikli yöntem olarak fatura e-posta/SMS bildirimleri parse edilecek; anlık kullanım için kendi hesabınla giriş yapılan bir tarayıcı otomasyonu kullanılabilir."
      note="Resmi/genel kullanıma açık bir API bulunmadığından bu entegrasyon kırılgan olabilir ve Türk Telekom'un arayüz değişiklikleriyle bozulabilir."
    />
  );
}
