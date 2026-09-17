import { useState } from "react";

function Home() {
  const [repoUrl, setRepoUrl] = useState("");

  return (
    <main>
      <h1>Analyze Your GitHub Repository</h1>

      <p>
        Enter your GitHub repository URL to analyze its health.
      </p>

      <input
        type="text"
        placeholder="https://github.com/user/project"
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
      />
        <button>
           Analyze Repository
        </button>
    </main>
  );
}

export default Home;