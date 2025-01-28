# CURSED WORDS SRT

## detecting cursed words in SRT Substile file using python

<hr>

Berikut adalah tabel yang merangkum method Python yang relevan dengan proyek Anda, khususnya untuk manipulasi string dan operasi lainnya yang berkaitan dengan proyek ini:

| **Kategori**          | **Method/Fungsi**        | **Deskripsi**                                                                                | **Contoh Penggunaan**                                                                 |
| --------------------- | ------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Manipulasi String** | `str.split()`            | Memisahkan string menjadi list berdasarkan delimiter (default: spasi).                       | `words = "I might skip this shit".split()` → `['I', 'might', 'skip', 'this', 'shit']` |
|                       | `str.join()`             | Menggabungkan list of strings menjadi satu string dengan delimiter.                          | `" ".join(['I', 'might', 'skip', 'this', 'sh*t'])` → `"I might skip this sh*t"`       |
|                       | `str.replace(old, new)`  | Mengganti substring `old` dengan `new` dalam sebuah string.                                  | `"shit".replace("shit", "sh*t")` → `"sh*t"`                                           |
|                       | `str.lower()`            | Mengubah string menjadi lowercase.                                                           | `"Shit".lower()` → `"shit"`                                                           |
|                       | `str.upper()`            | Mengubah string menjadi uppercase.                                                           | `"shit".upper()` → `"SHIT"`                                                           |
|                       | `str.strip()`            | Menghapus whitespace (spasi, newline, dll.) di awal dan akhir string.                        | `"  shit  ".strip()` → `"shit"`                                                       |
|                       | `str.startswith(prefix)` | Mengecek apakah string diawali dengan `prefix`.                                              | `"shit".startswith("sh")` → `True`                                                    |
|                       | `str.endswith(suffix)`   | Mengecek apakah string diakhiri dengan `suffix`.                                             | `"shit".endswith("it")` → `True`                                                      |
| **Pencarian String**  | `str.find(sub)`          | Mencari indeks pertama kemunculan substring `sub`. Jika tidak ditemukan, mengembalikan `-1`. | `"shit".find("hi")` → `1`                                                             |
|                       | `str.count(sub)`         | Menghitung jumlah kemunculan substring `sub` dalam string.                                   | `"shit shit".count("shit")` → `2`                                                     |
|                       | `sub in str`             | Mengecek apakah substring `sub` ada dalam string.                                            | `"shit" in "I hate shit"` → `True`                                                    |
| **List Operations**   | `list.append(item)`      | Menambahkan `item` ke akhir list.                                                            | `result_words.append("I might skip this sh*t")`                                       |
|                       | `list.extend(iterable)`  | Menambahkan semua elemen dari `iterable` ke list.                                            | `result_words.extend(["I", "might", "skip"])`                                         |
|                       | `list.index(item)`       | Mengembalikan indeks pertama dari `item` dalam list.                                         | `forbidden_list.index("shit")` → `2` (jika "shit" ada di indeks 2)                    |
|                       | `item in list`           | Mengecek apakah `item` ada dalam list.                                                       | `"shit" in forbidden_list` → `True`                                                   |
| **File Handling**     | `open(file, mode)`       | Membuka file dengan mode tertentu (`r` untuk read, `w` untuk write, dll.).                   | `with open("sub.srt", "r") as file: ...`                                              |
|                       | `file.read()`            | Membaca seluruh konten file sebagai string.                                                  | `content = file.read()`                                                               |
|                       | `file.readlines()`       | Membaca file baris per baris dan mengembalikan list of strings.                              | `lines = file.readlines()`                                                            |
|                       | `file.write(string)`     | Menulis string ke file.                                                                      | `file.write("I might skip this sh*t")`                                                |
| **Library pysrt**     | `pysrt.open(file)`       | Membuka file SRT dan mengembalikan objek subtitle.                                           | `subs = pysrt.open("sub.srt")`                                                        |
|                       | `sub.text`               | Mengambil teks dari sebuah subtitle.                                                         | `text = sub.text`                                                                     |
|                       | `sub.start`              | Mengambil waktu mulai subtitle.                                                              | `start_time = sub.start`                                                              |
|                       | `sub.end`                | Mengambil waktu berakhir subtitle.                                                           | `end_time = sub.end`                                                                  |

---

### **Catatan Penting:**

1. **Manipulasi String**: Anda akan sering menggunakan `split()`, `join()`, dan `replace()` untuk memproses teks subtitle.
2. **Pencarian String**: Gunakan `in` untuk mengecek apakah sebuah kata ada di `forbidden_list`.
3. **List Operations**: `append()` dan `extend()` akan berguna untuk menyimpan hasil manipulasi string.
4. **File Handling**: Jika Anda perlu membaca atau menulis file SRT, pastikan Anda memahami cara menggunakan `open()`, `read()`, dan `write()`.
5. **Library pysrt**: Library ini sangat berguna untuk membaca dan memanipulasi file SRT. Pastikan Anda sudah menginstalnya (`pip install pysrt`).

---

Jika ada method atau konsep yang masih kurang jelas, silakan tanyakan! 😊
