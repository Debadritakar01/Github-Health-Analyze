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
  const response = await fetch(
    "http://127.0.0.1:8000/analyze",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        repo_url: repoUrl,
      }),
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.detail || "Something went wrong."
    );
  }

  setRepository(data.repository);
  setHealthScore(data.health_score);
} catch (err) {
  console.error("Analyze error:", err);

  setError(
    err.message ||
      "Unable to connect to the backend. Make sure FastAPI is running."
  );
} finally {
  setLoading(false);
}

};

// Documentation
const documentationScore =
healthScore?.documentation?.score ?? 0;

const documentationDetails =
healthScore?.documentation?.details ?? [];

// Testing
const testingScore =
healthScore?.testing?.score ?? 0;

const testingDetails =
healthScore?.testing?.details ?? [];

// Security
const securityScore =
healthScore?.security?.score ?? 0;

const securityDetails =
healthScore?.security?.details ?? [];

// Overall Score
const overallScore =
documentationScore +
testingScore +
(healthScore?.code_structure ?? 0) +
securityScore +
(healthScore?.maintainability ?? 0);

return ( <main id="home" className="home">


  <section className="hero">

    <p className="badge">
      GitHub Repository Analysis
    </p>

    <h1>
      Analyze Your GitHub Repository
    </h1>

    <p className="hero-text">
      Enter a GitHub repository URL and get useful information
      about your repository's health, structure, and development
      activity.
    </p>

    <div id="analyzer" className="analyzer-box">

      <input
        type="text"
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
        placeholder="https://github.com/username/repository"
      />

      <button
        onClick={analyzeRepository}
        disabled={loading}
      >
        {loading
          ? "Analyzing..."
          : "Analyze Repository"}
      </button>

    </div>

    {error && (
      <p className="error-message">
        {error}
      </p>
    )}

  </section>


  {repository && (
    <section className="result-section">

      {/* Health Score */}

      {healthScore && (
        <div className="health-score-card">

          <h2>
            Repository Health Score
          </h2>

          <div className="score-cards">

            {/* Documentation */}

            <div className="score-card">
              <div className="score">
                {documentationScore}/20
              </div>
              <p>Documentation</p>
            </div>

            {/* Testing */}

            <div className="score-card">
              <div className="score">
                {testingScore}/20
              </div>
              <p>Testing</p>
            </div>

            {/* Code Structure */}

            <div className="score-card">
              <div className="score">
                {healthScore.code_structure ?? 0}/20
              </div>
              <p>Code Structure</p>
            </div>

            {/* Security */}

            <div className="score-card">
              <div className="score">
                {securityScore}/20
              </div>
              <p>Security</p>
            </div>

            {/* Maintainability */}

            <div className="score-card">
              <div className="score">
                {healthScore.maintainability ?? 0}/20
              </div>
              <p>Maintainability</p>
            </div>

          </div>

          <div className="overall-score">

            <h3>
              Repository Health Score
            </h3>

            <div className="overall-number">
              {overallScore}/100
            </div>

            <p>
              Based on all five health categories
            </p>

          </div>

        </div>
      )}


      {/* Documentation Analysis */}

      {healthScore?.documentation && (
        <div className="documentation-details">

          <h2>
            Documentation Analysis
          </h2>

          <div className="documentation-score">
            Documentation Score:{" "}
            <strong>
              {documentationScore}/20
            </strong>
          </div>

          <div className="documentation-findings">

            {documentationDetails.map(
              (detail, index) => (
                <div
                  key={index}
                  className={`documentation-item ${detail.type}`}
                >

                  <span className="documentation-icon">
                    {detail.type === "success"
                      ? "✓"
                      : "⚠"}
                  </span>

                  <span>
                    {detail.message}
                  </span>

                </div>
              )
            )}

          </div>

        </div>
      )}


      {/* Testing Analysis */}

      {healthScore?.testing && (
        <div className="testing-details">

          <h2>
            Testing Analysis
          </h2>

          <div className="testing-score">
            Testing Score:{" "}
            <strong>
              {testingScore}/20
            </strong>
          </div>

          <div className="testing-findings">

            {testingDetails.map(
              (detail, index) => (
                <div
                  key={index}
                  className={`testing-item ${detail.type}`}
                >

                  <span className="testing-icon">
                    {detail.type === "success"
                      ? "✓"
                      : "⚠"}
                  </span>

                  <span>
                    {detail.message}
                  </span>

                </div>
              )
            )}

          </div>

        </div>
      )}


      {/* Security Analysis */}

      {healthScore?.security && (
        <div className="security-details">

          <h2>
            Security Analysis
          </h2>

          <div className="security-score">
            Security Score:{" "}
            <strong>
              {securityScore}/20
            </strong>
          </div>

          <div className="security-findings">

            {securityDetails.map(
              (detail, index) => (
                <div
                  key={index}
                  className={`security-item ${detail.type}`}
                >

                  <span className="security-icon">
                    {detail.type === "success"
                      ? "✓"
                      : "⚠"}
                  </span>

                  <span>
                    {detail.message}
                  </span>

                </div>
              )
            )}

          </div>

        </div>
      )}


      {/* Repository Information */}

      <h2>
        Repository Information
      </h2>

      <div className="repository-card">

        <h3>
          {repository.name}
        </h3>

        <p className="full-name">
          {repository.full_name}
        </p>

        <p>
          {repository.description ||
            "No description available."}
        </p>

        <div className="stats">

          <div className="stat-card">
            <strong>
              {repository.language || "N/A"}
            </strong>
            <span>Language</span>
          </div>

          <div className="stat-card">
            <strong>
              {repository.stars}
            </strong>
            <span>Stars</span>
          </div>

          <div className="stat-card">
            <strong>
              {repository.forks}
            </strong>
            <span>Forks</span>
          </div>

          <div className="stat-card">
            <strong>
              {repository.open_issues}
            </strong>
            <span>Open Issues</span>
          </div>

        </div>

        <div className="repository-details">

          <p>
            <strong>
              Default Branch:
            </strong>{" "}
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
