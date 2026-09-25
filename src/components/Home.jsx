
import { useState } from "react";

function Home() {
  const [repoUrl, setRepoUrl] = useState("");
  const [repository, setRepository] = useState(null);
  const [healthScore, setHealthScore] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeRepository = async () => {
    if (!repoUrl.trim()) {
      setError("Please enter a GitHub repository URL.");
      return;
    }

    setLoading(true);
    setError("");
    setRepository(null);
    setHealthScore(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          repo_url: repoUrl,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong.");
      }

      setRepository(data.repository);
      setHealthScore(data.health_score);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect to the backend. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main id="home" className="home">
      <section className="hero">
        <p className="badge">GitHub Repository Analysis</p>

        <h1>Analyze Your GitHub Repository</h1>

        <p className="hero-text">
          Enter a GitHub repository URL and get useful information about your
          repository's health, structure, and development activity.
        </p>

        <div id="analyzer" className="analyzer-box">
          <input
            type="text"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            placeholder="https://github.com/username/repository"
          />

          <button onClick={analyzeRepository} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze Repository"}
          </button>
        </div>

        {error && <p className="error-message">{error}</p>}
      </section>

      {repository && (
  <section className="result-section">

    {healthScore && (
      <div className="health-score-card">
        <h2>Repository Health Score</h2>

        <div className="score">
          {healthScore.documentation}/20
        </div>

        <p>Documentation</p>
      </div>
    )}

    <h2>Repository Information</h2>

          <div className="repository-card">
            <h3>{repository.name}</h3>

            <p className="full-name">{repository.full_name}</p>

            <p>
              {repository.description || "No description available."}
            </p>

            <div className="stats">
              <div className="stat-card">
                <strong>{repository.language || "N/A"}</strong>
                <span>Language</span>
              </div>

              <div className="stat-card">
                <strong>{repository.stars}</strong>
                <span>Stars</span>
              </div>

              <div className="stat-card">
                <strong>{repository.forks}</strong>
                <span>Forks</span>
              </div>

              <div className="stat-card">
                <strong>{repository.open_issues}</strong>
                <span>Open Issues</span>
              </div>
            </div>

            <div className="repository-details">
              <p>
                <strong>Default Branch:</strong>{" "}
                {repository.default_branch || "N/A"}
              </p>

              <a
                href={repoUrl}
                target="_blank"
                rel="noopener noreferrer"
              >
                View Repository on GitHub →
              </a>
            </div>
          </div>
        </section>
      )}
    </main>
  );
}

export default Home;
