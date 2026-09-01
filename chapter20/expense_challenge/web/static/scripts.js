const form = document.getElementById("expense-form");
const tbody = document.getElementById("expense-body");
const totalEl = document.getElementById("total");
const errorEl = document.getElementById("error-msg");
const searchInput = document.getElementById("search-input");

let allExpenses = [];   // 서버에서 받아온 전체 데이터를 여기 보관

// 표를 그리는 부분만 별도 함수로 분리 (렌더링 전담)
function renderExpenses(expenses) {
  tbody.innerHTML = "";
  let total = 0;

  for (const e of expenses) {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${e.date}</td>
      <td>${e.category}</td>
      <td>${e.description}</td>
      <td>${e.amount}원</td>
    `;
    tbody.appendChild(row);
    total += e.amount;
  }

  totalEl.textContent = total;
}

// 검색어로 필터링
function applySearch() {
  const keyword = searchInput.value.trim().toLowerCase();

  if (keyword === "") {
    renderExpenses(allExpenses);
    return;
  }

  const filtered = allExpenses.filter((e) =>
    e.category.toLowerCase().includes(keyword) ||
    e.description.toLowerCase().includes(keyword)
  );

  renderExpenses(filtered);
}

// 서버에서 목록 불러오기
async function loadExpenses() {
  const res = await fetch("/api/expenses");
  allExpenses = await res.json();
  applySearch();   // 불러온 직후에도 현재 검색어 기준으로 그리기
}

// 입력할 때마다 실시간 필터링
searchInput.addEventListener("input", applySearch);

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  errorEl.textContent = "";

  const formData = new FormData(form);
  const payload = {
    date: formData.get("date"),
    category: formData.get("category"),
    description: formData.get("description"),
    amount: formData.get("amount"),
  };

  const res = await fetch("/api/expenses", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const err = await res.json();
    errorEl.textContent = err.error;
    return;
  }

  form.reset();
  loadExpenses();
});

loadExpenses();