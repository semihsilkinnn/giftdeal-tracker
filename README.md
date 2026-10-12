# GiftDeal Tracker — ücretsiz otomatik keşif

## Kurulum (bir kez)
1. Ücretsiz GitHub hesabı açın.
2. **Public** yeni repository oluşturun (ör. `giftdeal-tracker`). Bu repo herkese açıktır; kişisel bilgi koymayın.
3. Bu ZIP içindeki **tüm dosya ve klasörleri** (gizli `.github` klasörü dahil) repository köküne yükleyin.
4. GitHub **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**.
5. **Actions → Refresh deals → Run workflow** ile ilk taramayı çalıştırın. Workflow'ın repo içeriğine yazma izni gerekirse **Settings → Actions → General → Workflow permissions → Read and write permissions** seçin.
6. Actions başarılı olunca birkaç dakika içinde `https://KULLANICI.github.io/giftdeal-tracker/` adresinden Safari'de açın. Paylaş → Ana Ekrana Ekle.

## Özellikler ve sınırlar
- RSS üzerinden Slickdeals Frontpage ve 9to5Toys fırsatları taranır. Site politikaları, ağ kesintisi veya RSS değişikliği veri toplamayı durdurabilir.
- GitHub Actions yaklaşık 3 saatte bir çalışır; kesin saat garantisi yoktur. Public repository'de standart runner ücretsizdir (GitHub koşullarına tabidir).
- Mağaza fiyatlarını doğrudan doğrulamaz; yalnızca ilan başlığındaki ilk USD tutarını gösterir. Kargo, vergi, kupon, üyelik ve stok koşulları farklı olabilir.
- Safari favorileri cihazın localStorage alanında saklanır; cihazlar arası senkronize olmaz.
- Push bildirim, fiyat geçmişi, bütün internet taraması, Türkiye fiyat kıyaslaması yoktur.
- GitHub Pages'te doğrudan çalışır; yerel dosya olarak açıldığında tarama JSON'u yüklenmeyebilir.
