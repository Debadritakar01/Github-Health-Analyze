
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

  // =========================
  // Documentation
  // =========================

  const documentationScore =
    healthScore?.documentation?.score ?? 0;

  const documentationDetails =
    healthScore?.documentation?.details ?? [];

  // =========================
  // Testing
  // =========================

  const testingScore =
    healthScore?.testing?.score ?? 0;

  const testingDetails =
    healthScore?.testing?.details ?? [];

  // =========================
  // Code Structure
  // =========================

  const codeStructureScore =
    healthScore?.code_structure?.score ?? 0;

  const codeStructureDetails =
    healthScore?.code_structure?.details ?? [];

  // =========================
  // Security
  // =========================

  const securityScore =
    healthScore?.security?.score ?? 0;

  const securityDetails =
    healthScore?.security?.details ?? [];

  // =========================
  // Maintainability
  // =========================

  const maintainabilityScore =
    healthScore?.maintainability?.score ?? 0;

  const maintainabilityDetails =
    healthScore?.maintainability?.details ?? [];

  // =========================
  // Overall Score
  // =========================

  const overallScore =
    documentationScore +
    testingScore +
    codeStructureScore +
    securityScore +
    maintainabilityScore;

  return (
    <main id="home" className="home">

      {/* =========================
          HERO SECTION
      ========================= */}

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

        <div
          id="analyzer"
          className="analyzer-box"
        >

          <input
            type="text"
            value={repoUrl}
            onChange={(e) =>
              setRepoUrl(e.target.value)
            }
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


      {/* =========================
          RESULT SECTION
      ========================= */}

      {repository && (

        <section className="result-section">

          {/* =========================
              HEALTH SCORE DASHBOARD
          ========================= */}

          {healthScore && (

            <div className="health-score-card">

              <h2>
                Repository Health Score
              </h2>


              {/* =========================
                  OVERALL SCORE
              ========================= */}

              <div className="overall-score-card">

                <div className="overall-score-header">

                  <div>
                    <h3>
                      Repository Health
                    </h3>

                    <p>
                      Overall repository quality
                    </p>
                  </div>

                  <div className="overall-score-number">
                    {overallScore}
                    <span>/100</span>
                  </div>

                </div>


                <div className="score-progress">

                  <div
                    className="score-progress-fill"
                    style={{
                      width: `${overallScore}%`
                    }}
                  ></div>

                </div>

              </div>


              {/* =========================
                  CATEGORY SCORE CARDS
              ========================= */}

              <div className="score-cards">

                {/* Documentation */}

                <div className="score-card">

                  <div className="score">
                    {documentationScore}/20
                  </div>

                  <p>
                    Documentation
                  </p>

                </div>


                {/* Testing */}

                <div className="score-card">

                  <div className="score">
                    {testingScore}/20
                  </div>

                  <p>
                    Testing
                  </p>

                </div>


                {/* Code Structure */}

                <div className="score-card">

                  <div className="score">
                    {codeStructureScore}/20
                  </div>

                  <p>
                    Code Structure
                  </p>

                </div>


                {/* Security */}

                <div className="score-card">

                  <div className="score">
                    {securityScore}/20
                  </div>

                  <p>
                    Security
                  </p>

                </div>


                {/* Maintainability */}

                <div className="score-card">

                  <div className="score">
                    {maintainabilityScore}/20
                  </div>

                  <p>
                    Maintainability
                  </p>

                </div>

              </div>


              {/* =========================
                  CATEGORY PROGRESS BARS
              ========================= */}

              <div className="category-scores">

                {/* Documentation */}

                <div className="category-score">

                  <div className="category-score-header">

                    <span>
                      Documentation
                    </span>

                    <span>
                      {documentationScore}/20
                    </span>

                  </div>

                  <div className="category-progress">

                    <div
                      className="category-progress-fill"
                      style={{
                        width: `${documentationScore * 5}%`
                      }}
                    ></div>

                  </div>

                </div>


                {/* Testing */}

                <div className="category-score">

                  <div className="category-score-header">

                    <span>
                      Testing
                    </span>

                    <span>
                      {testingScore}/20
                    </span>

                  </div>

                  <div className="category-progress">

                    <div
                      className="category-progress-fill"
                      style={{
                        width: `${testingScore * 5}%`
                      }}
                    ></div>

                  </div>

                </div>


                {/* Code Structure */}

                <div className="category-score">

                  <div className="category-score-header">

                    <span>
                      Code Structure
                    </span>

                    <span>
                      {codeStructureScore}/20
                    </span>

                  </div>

                  <div className="category-progress">

                    <div
                      className="category-progress-fill"
                      style={{
                        width: `${codeStructureScore * 5}%`
                      }}
                    ></div>

                  </div>

                </div>


                {/* Security */}

                <div className="category-score">

                  <div className="category-score-header">

                    <span>
                      Security
                    </span>

                    <span>
                      {securityScore}/20
                    </span>

                  </div>

                  <div className="category-progress">

                    <div
                      className="category-progress-fill"
                      style={{
                        width: `${securityScore * 5}%`
                      }}
                    ></div>

                  </div>

                </div>


                {/* Maintainability */}

                <div className="category-score">

                  <div className="category-score-header">

                    <span>
                      Maintainability
                    </span>

                    <span>
                      {maintainabilityScore}/20
                    </span>

                  </div>

                  <div className="category-progress">

                    <div
                      className="category-progress-fill"
                      style={{
                        width: `${maintainabilityScore * 5}%`
                      }}
                    ></div>

                  </div>

                </div>

              </div>

            </div>

          )}


          {/* =========================
              DOCUMENTATION ANALYSIS
          ========================= */}

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


          {/* =========================
              TESTING ANALYSIS
          ========================= */}

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


          {/* =========================
              CODE STRUCTURE ANALYSIS
          ========================= */}

          {healthScore?.code_structure && (

            <div className="code-structure-details">

              <h2>
                Code Structure Analysis
              </h2>

              <div className="code-structure-score">

                Code Structure Score:{" "}

                <strong>
                  {codeStructureScore}/20
                </strong>

              </div>

              <div className="code-structure-findings">

                {codeStructureDetails.map(
                  (detail, index) => (

                    <div
                      key={index}
                      className={`code-structure-item ${detail.type}`}
                    >

                      <span className="code-structure-icon">

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


          {/* =========================
              SECURITY ANALYSIS
          ========================= */}

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


          {/* =========================
              MAINTAINABILITY ANALYSIS
          ========================= */}

          {healthScore?.maintainability && (

            <div className="maintainability-details">

              <h2>
                Maintainability Analysis
              </h2>

              <div className="maintainability-score">

                Maintainability Score:{" "}

                <strong>
                  {maintainabilityScore}/20
                </strong>

              </div>

              <div className="maintainability-findings">

                {maintainabilityDetails.map(
                  (detail, index) => (

                    <div
                      key={index}
                      className={`maintainability-item ${detail.type}`}
                    >

                      <span className="maintainability-icon">

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


          {/* =========================
              REPOSITORY INFORMATION
              UPDATED SECTION
          ========================= */}

          <div className="repository-section">

            <div className="section-title">

              <h2>
                Repository Information
              </h2>

              <p>
                Details about the analyzed GitHub repository
              </p>

            </div>


            <div className="repository-info-grid">

              {/* Repository Name */}

              <div className="repository-info-card">

                <span className="info-label">
                  Repository
                </span>

                <strong>
                  {repository.name || "N/A"}
                </strong>

              </div>


              {/* Language */}

              <div className="repository-info-card">

                <span className="info-label">
                  Language
                </span>

                <strong>
                  {repository.language || "N/A"}
                </strong>

              </div>


              {/* Stars */}

              <div className="repository-info-card">

                <span className="info-label">
                  Stars
                </span>

                <strong>
                  {repository.stars ?? 0}
                </strong>

              </div>


              {/* Forks */}

              <div className="repository-info-card">

                <span className="info-label">
                  Forks
                </span>

                <strong>
                  {repository.forks ?? 0}
                </strong>

              </div>


              {/* Open Issues */}

              <div className="repository-info-card">

                <span className="info-label">
                  Open Issues
                </span>

                <strong>
                  {repository.open_issues ?? 0}
                </strong>

              </div>


              {/* Default Branch */}

              <div className="repository-info-card">

                <span className="info-label">
                  Default Branch
                </span>

                <strong>
                  {repository.default_branch || "N/A"}
                </strong>

              </div>

            </div>


            {/* Repository Description */}

            <div className="repository-description">

              <span className="info-label">
                Description
              </span>

              <p>
                {repository.description ||
                  "No repository description available."}
              </p>

            </div>


            {/* GitHub Repository Link */}

            <div className="repository-link">

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
