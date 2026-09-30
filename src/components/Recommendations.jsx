function Recommendations({ recommendations = [] }) {

  if (recommendations.length === 0) {
    return (
      <section className="recommendations-section">

        <div className="section-title">
          <h2>Recommendations</h2>

          <p>
            No improvement recommendations were generated.
          </p>
        </div>

      </section>
    );
  }


  return (
    <section className="recommendations-section">

      <div className="section-title">

        <h2>Recommendations</h2>

        <p>
          Actionable suggestions based on the repository analysis.
        </p>

      </div>


      <div className="recommendations-list">

        {recommendations.map((item, index) => (

          <div
            className="recommendation-card"
            key={index}
          >

            {/* Recommendation Header */}

            <div className="recommendation-header">

              <span className="recommendation-category">
                {item.category}
              </span>

              <span
                className={`recommendation-priority ${
                  item.priority?.toLowerCase()
                }`}
              >
                {item.priority}
              </span>

            </div>


            {/* Detected Issue */}

            <div className="recommendation-message">

              <strong>
                Detected Issue
              </strong>

              <p>
                {item.message}
              </p>

            </div>


            {/* Recommendation */}

            <div className="recommendation-action">

              <strong>
                Recommended Action
              </strong>

              <p>
                {item.recommendation}
              </p>

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}


export default Recommendations;