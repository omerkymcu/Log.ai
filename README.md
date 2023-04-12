# Log.ai
Log Checker


Bu Python programı, belirli bir klasördeki log dosyalarını okur ve içinde "error" kelimesi geçen satırları bulur. Bu satırlar, dosya adı, satır numarası ve içerik bilgileriyle birlikte bir listede saklanır. Eğer log dosyalarında hata yoksa, "No errors found." şeklinde bir çıktı verir.

Eğer log dosyalarında hata varsa, program bir grafik arayüzünde (GUI) kullanıcıya hata içeren satırları gösterir. Bu pencerede, her bir hata satırı dosya adı, satır numarası ve içerik bilgileriyle birlikte görüntülenir.

Ayrıca, program dosyaların karakter kodlamalarını otomatik olarak algılar ve uygun şekilde açar.

Programın kullanımı oldukça basittir. Kullanıcı, bir dosya gezgini aracılığıyla okunacak log dosyalarının klasörünü seçer. Program, klasördeki tüm uygun dosyaları otomatik olarak tespit eder ve işlemeye başlar.

Bu program, Python 3 kullanılarak yazılmıştır ve Tkinter ve chardet kütüphanelerini kullanır.
