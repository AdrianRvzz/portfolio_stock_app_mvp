import React, { useEffect, useState } from "react";
import { PieChart, Pie, Cell, Tooltip, Legend } from "recharts";

const API_URL = "https://portfolio-pink-nine-zqqb57t52q.vercel.app";
const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#AA336A"];

export default function Portfolio() {
  const [portfolio, setPortfolio] = useState(null);
  const [key, setKey] = useState("");
  const [price, setPrice] = useState("");

  const fetchPortfolio = async () => {
    const res = await fetch(`${API_URL}/portfolio`);
    const data = await res.json();
    setPortfolio(data);
  };

  useEffect(() => {
    fetchPortfolio();
  }, []);

  const updatePrice = async (e) => {
    e.preventDefault();

    const res = await fetch(`${API_URL}/update_price`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        key,
        price: Number(price),
      }),
    });

    const data = await res.json();
    setPortfolio(data);
    setKey("");
    setPrice("");
  };

  const restartPortfolio = async (e) => {
  e.preventDefault();
  const res = await fetch(`${API_URL}/restart`, {
    method: "POST",
  });
  const data = await res.json();
  setPortfolio(data);
};
  if (!portfolio) return <p>Loading portfolio...</p>;

  // ---- Quantity-based allocation ----
  const totalQuantity = Object.values(portfolio.invests).reduce(
    (sum, info) => sum + info.quantity,
    0
  );

  const tableData = Object.entries(portfolio.invests).map(([stockKey, info]) => {
    const percentage = (info.quantity / totalQuantity) * 100;

    return {
      key: stockKey,
      quantity: info.quantity.toFixed(2),
      price: info.price.toFixed(2),
      percentage: percentage.toFixed(1),
    };
  });

  const pieData = tableData.map((item) => ({
    name: item.key,
    value: Number(item.percentage),
  }));

  return (
    <div style={{ maxWidth: "800px", margin: "0 auto", fontFamily: "Arial" }}>
      <h2>Portfolio</h2>
      <p>Total Value: ${portfolio.total_value.toFixed(2)}</p>

      {/* ---- Simple update form ---- */}
      <form onSubmit={updatePrice} style={{ marginBottom: "20px" }}>
        <input
          placeholder="Stock key (e.g. AAPL)"
          value={key}
          onChange={(e) => setKey(e.target.value)}
        />

        <input
          type="number"
          step="0.01"
          placeholder="New price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          style={{ marginLeft: "10px" }}
        />

        <button type="submit" style={{ marginLeft: "10px" }}>
          Update
        </button>
        <button onClick={restartPortfolio} style={{ marginBottom: "20px" }}>
  Restart Portfolio
</button>
      </form>

      {/* ---- Table ---- */}
      <table border="1" width="100%" cellPadding="8" cellSpacing="0">
        <thead>
          <tr>
            <th>Stock</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>% of Shares</th>
          </tr>
        </thead>
        <tbody>
          {tableData.map((row) => (
            <tr key={row.key}>
              <td>{row.key}</td>
              <td>{row.quantity}</td>
              <td>${row.price}</td>
              <td>{row.percentage}%</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* ---- Pie Chart (quantity-based) ---- */}
      <PieChart width={400} height={400}>
        <Pie
          data={pieData}
          dataKey="value"
          nameKey="name"
          cx="50%"
          cy="50%"
          outerRadius={130}
          label
        >
          {pieData.map((_, index) => (
            <Cell key={index} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>
        <Tooltip formatter={(v) => `${v.toFixed(1)}%`} />
        <Legend />
      </PieChart>
    </div>
  );
}
