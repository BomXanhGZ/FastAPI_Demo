import { useEffect, useMemo, useState } from "react";

const API = import.meta.env.VITE_API_URL || "";

const TOKEN_KEY = "login-demo-token";

function formatJson(value) {
  return JSON.stringify(value, null, 2);
}

async function parseResponse(response) {
  const text = await response.text();
  const data = text ? JSON.parse(text) : null;

  if (!response.ok) {
    const detail = data?.detail || data?.error?.message || response.statusText;
    throw new Error(`${response.status} ${detail}`);
  }

  return data;
}

export default function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState(() => localStorage.getItem(TOKEN_KEY) || "");
  const [currentUser, setCurrentUser] = useState(null);
  const [result, setResult] = useState("Ket qua API se hien thi o day.");
  const [loading, setLoading] = useState(false);

  const authHeaders = useMemo(() => {
    return token ? { Authorization: `Bearer ${token}` } : {};
  }, [token]);

  async function api(path, options = {}) {
    const response = await fetch(`${API}${path}`, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        ...authHeaders,
        ...options.headers,
      },
    });

    return parseResponse(response);
  }

  async function run(title, action) {
    try {
      setLoading(true);
      const data = await action();
      setResult(`${title}\n\n${formatJson(data)}`);
      return data;
    } catch (error) {
      setResult(`Loi API\n\n${formatJson({ message: error.message })}`);
      return null;
    } finally {
      setLoading(false);
    }
  }

  function getCredentials() {
    return {
      username: username.trim(),
      password,
    };
  }

  async function register() {
    await run("Dang ky thanh cong", () =>
      api("/register", {
        method: "POST",
        body: JSON.stringify(getCredentials()),
      }),
    );
  }

  async function login(event) {
    event.preventDefault();

    const data = await run("Dang nhap thanh cong", () =>
      api("/login", {
        method: "POST",
        body: JSON.stringify(getCredentials()),
      }),
    );

    if (data?.access_token) {
      setToken(data.access_token);
      localStorage.setItem(TOKEN_KEY, data.access_token);
    }
  }

  async function loadMe() {
    const data = await run("Thong tin /me", () => api("/me"));
    if (data) {
      setCurrentUser(data);
    }
  }

  function logout() {
    setToken("");
    setCurrentUser(null);
    localStorage.removeItem(TOKEN_KEY);
    setResult(`Da dang xuat\n\n${formatJson({ token: null })}`);
  }

  useEffect(() => {
    if (!token) {
      return;
    }

    loadMe();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  return (
    <main className="shell">
      <section className="panel auth-panel">
        <div>
          <p className="eyebrow">FastAPI Auth Demo</p>
          <h1>Frontend React de test dang ky, dang nhap</h1>
        </div>

        <form className="form" onSubmit={login}>
          <label>
            Username
            <input
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              type="text"
              autoComplete="username"
              required
            />
          </label>

          <label>
            Password
            <input
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              type="password"
              autoComplete="current-password"
              required
            />
          </label>

          <div className="actions">
            <button type="button" onClick={register} disabled={loading}>
              Dang ky
            </button>
            <button type="submit" disabled={loading}>
              Dang nhap
            </button>
          </div>
        </form>
      </section>

      <section className="panel status-panel">
        <div className="status-header">
          <div>
            <p className="eyebrow">Tai khoan hien tai</p>
            <h2>
              {currentUser
                ? `${currentUser.username} (#${currentUser.id})`
                : "Chua dang nhap"}
            </h2>
          </div>
          <button
            type="button"
            className="secondary"
            onClick={logout}
            disabled={loading}
          >
            Dang xuat
          </button>
        </div>

        <div className="token-box">
          <span>Token</span>
          <code>{token || "Chua co token"}</code>
        </div>

        <div className="actions">
          <button type="button" onClick={loadMe} disabled={loading || !token}>
            Goi /me
          </button>
          <a href={`${API}/docs`} target="_blank" rel="noreferrer">
            Mo Swagger
          </a>
        </div>

        <pre aria-live="polite">{result}</pre>
      </section>
    </main>
  );
}