# 🏫 Government Senior Secondary School Tamber — Website

Professional 5-page school website built with pure HTML, CSS & JavaScript.  
Teen alag files mein structured — aasaan customization ke liye.

---

## 📁 Project Structure

```
school-website/
├── index.html    ← Saara HTML (pages ka content)
├── styles.css    ← Saari CSS (colors, layout, design)
├── script.js     ← Saara JavaScript (page navigation)
└── README.md
```

> ⚠️ Teeno files ek hi folder mein honi chahiye — warna website sahi se nahi chalegi.

---

## 📄 Pages

| Page | ID | Kya dikhta hai |
|------|----|----------------|
| 🏠 Home | `#home` | Hero, stats, features |
| 🏛️ About | `#about` | History, principal message, faculty |
| 📚 Classes | `#classes` | Facilities, class structure table |
| 📝 Admission | `#admission` | Steps, inquiry form, fee structure |
| 📞 Contact | `#contact` | Address, timings, contact form |

---

## 🚀 Run Karna

### Option 1 — Seedha browser mein (without server)
```
index.html par double click karo → browser mein khulega
```

### Option 2 — Nginx Docker ke saath (recommended)
```bash
# Teeno files ko html/ folder mein rakho
cp index.html styles.css script.js nginx-static-project/html/

cd nginx-static-project
docker-compose up -d

# Browser mein kholo
open http://localhost:8080
```

---

## ✏️ Customization Guide

### 🎨 Colors badlna (`styles.css` — line 7 ke aas paas)
```css
:root {
  --navy:  #0a1f44;   /* Dark background color */
  --blue:  #1a56db;   /* Buttons & accents */
  --gold:  #f59e0b;   /* Highlights */
  --gray:  #64748b;   /* Paragraph text */
}
```
> Sirf yahan ek jagah color badlo — poori website update ho jaayegi.

---

### 📝 Content badlna (`index.html`)

| Kya badlna hai | Kahan milega |
|----------------|--------------|
| School ka naam | `<nav>` section + har page ka `<footer>` |
| Notice bar text | `class="notice-bar"` wala div |
| Stats (students, teachers) | `class="hero-stats"` wala section |
| Principal ka naam / message | About page — `about-text` div |
| Faculty ke naam | About page — `team-grid` div |
| Fee structure | Admission page — `fee-table` div |
| Address, phone, email | Contact page — `contact-info-card` div |
| School timings | Contact page — `timing-box` div |

---

### ⚙️ Naya Page Add Karna

1. `index.html` mein naya div banao:
```html
<div id="gallery" class="page">
  <!-- content yahan -->
</div>
```

2. Navbar mein link add karo:
```html
<li><a href="#" onclick="showPage('gallery', this)">Gallery</a></li>
```

3. `script.js` mein koi change nahi chahiye — automatically kaam karega ✅

---

## 🛠️ Tech Stack

| File | Kaam |
|------|------|
| `index.html` | Structure & content |
| `styles.css` | Saari styling — colors, layout, responsive |
| `script.js` | Page navigation (SPA style) |
| Google Fonts | Playfair Display + DM Sans |

---

## 📌 Notes

- Internet sirf Google Fonts ke liye chahiye — baaki sab offline bhi kaam karta hai
- Forms abhi frontend-only hain — backend ke liye PHP/Node.js baad mein connect karo
- Mobile responsive hai — chhote screen pe bhi sahi dikhta hai

---

*Built for Senior Secondary School Tamber — 2025*
