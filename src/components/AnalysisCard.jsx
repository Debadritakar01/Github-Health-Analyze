function AnalysisCard({
  title,
  score,
  details = [],
}) {
  return (
    <div className="analysis-card">

      {/* Header */}
      <div className="analysis-card-header">

        <div>
          <h2>{title}</h2>

          <p>
            Detailed analysis and findings
          </p>
        </div>

        <div className="analysis-card-score">
          {score}
          <span>/20</span>
        </div>

      </div>

      {/* Progress */}
      <div className="analysis-progress">

        <div
          className="analysis-progress-fill"
          style={{
            width: `${score * 5}%`,
          }}
        ></div>

      </div>

      {/* Findings */}
      <div className="analysis-findings">

        {details.length > 0 ? (

          details.map((detail, index) => (

            <div
              key={index}
              className={`analysis-item ${detail.type}`}
            >

              <span className="analysis-icon">

                {detail.type === "success"
                  ? "✓"
                  : "⚠"}

              </span>

              <span className="analysis-message">
                {detail.message}
              </span>

            </div>

          ))

        ) : (

          <div className="analysis-item warning">

            <span className="analysis-icon">
              ⚠
            </span>

            <span className="analysis-message">
              No detailed findings available.
            </span>

          </div>

        )}

      </div>

    </div>
  );
}

export default AnalysisCard;