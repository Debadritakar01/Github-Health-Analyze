import { useState } from "react";
import AnalysisCard from "./AnalysisCard";
import Recommendations from "./Recommendations";
function Home() {
  const [repoUrl, setRepoUrl] = useState("");
  const [repository, setRepository] = useState(null);
  const [healthScore, setHealthScore] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  // =========================
  // ANALYZE REPOSITORY
  // =========================

  const analyzeRepository = async () => {
    if (!repoUrl.trim()) {
      setError("Please enter a GitHub repository URL.");
      return;
    }

    setLoading(true);
    setError("");
    setRecommendations([]);
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
            repo_url: repoUrl.trim(),
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Failed to analyze repository."
        );
      }

      setRepository(data.repository);
      setHealthScore(data.health_score);
      setRecommendations(data.recommendations ?? []);

    } catch (error) {
      setError(
        error.message ||
        "Something went wrong while analyzing the repository."
      );
    } finally {
      setLoading(false);
    }
  };

  // =========================
  // DOCUMENTATION
  // =========================

  const documentationScore =
    healthScore?.documentation?.score ?? 0;

  const documentationDetails =
    healthScore?.documentation?.details ?? [];

  // =========================
  // TESTING
  // =========================

  const testingScore =
    healthScore?.testing?.score ?? 0;

  const testingDetails =
    healthScore?.testing?.details ?? [];

  // =========================
  // CODE STRUCTURE
  // =========================

  const codeStructureScore =
    healthScore?.code_structure?.score ?? 0;

  const codeStructureDetails =
    healthScore?.code_structure?.details ?? [];

  // =========================
  // SECURITY
  // =========================

  const securityScore =
    healthScore?.security?.score ?? 0;

  const securityDetails =
    healthScore?.security?.details ?? [];

  // =========================
  // MAINTAINABILITY
  // =========================

  const maintainabilityScore =
    healthScore?.maintainability?.score ?? 0;

  const maintainabilityDetails =
    healthScore?.maintainability?.details ?? [];

  // =========================
  // OVERALL SCORE
  // =========================

  const overallScore =
    healthScore?.overall ?? 0;

  return (
    <main
      id="home"
      className="home"
    >

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
          Enter a GitHub repository URL and get useful
          information about your repository's health,
          structure, and development activity.
        </p>

        {/* =========================
            ANALYZER INPUT
        ========================= */}

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
            disabled={loading}
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

        {/* =========================
            ERROR MESSAGE
        ========================= */}

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

                    <span>
                      /100
                    </span>

                  </div>

                </div>

                <div className="score-progress">

                  <div
                    className="score-progress-fill"
                    style={{
                      width: `${overallScore}%`,
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
                        width: `${documentationScore * 5}%`,
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
                        width: `${testingScore * 5}%`,
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
                        width: `${codeStructureScore * 5}%`,
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
                        width: `${securityScore * 5}%`,
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
                        width: `${maintainabilityScore * 5}%`,
                      }}
                    ></div>

                  </div>

                </div>

              </div>

            </div>

          )}


          {/* =========================
              DETAILED ANALYSIS
          ========================= */}

          {healthScore && (

            <div className="detailed-analysis-section">

              <div className="section-title">

                <h2>
                  Detailed Repository Analysis
                </h2>

                <p>
                  Review the strengths and areas for
                  improvement identified in each category.
                </p>

              </div>


              {/* =========================
                  ANALYSIS CARDS
              ========================= */}

              <div className="analysis-cards-grid">

                <AnalysisCard
                  title="Documentation"
                  score={documentationScore}
                  details={documentationDetails}
                />

                <AnalysisCard
                  title="Testing"
                  score={testingScore}
                  details={testingDetails}
                />

                <AnalysisCard
                  title="Code Structure"
                  score={codeStructureScore}
                  details={codeStructureDetails}
                />

                <AnalysisCard
                  title="Security"
                  score={securityScore}
                  details={securityDetails}
                />

                <AnalysisCard
                  title="Maintainability"
                  score={maintainabilityScore}
                  details={maintainabilityDetails}
                />

              </div>

            </div>

          )}
          {healthScore && (
              <Recommendations
                recommendations={recommendations}
              />
            )}

          {/* =========================
              REPOSITORY INFORMATION
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


            {/* =========================
                REPOSITORY INFO GRID
            ========================= */}

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


            {/* =========================
                DESCRIPTION
            ========================= */}

            <div className="repository-description">

              <span className="info-label">
                Description
              </span>

              <p>
                {repository.description ||
                  "No repository description available."}
              </p>

            </div>


            {/* =========================
                GITHUB LINK
            ========================= */}

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