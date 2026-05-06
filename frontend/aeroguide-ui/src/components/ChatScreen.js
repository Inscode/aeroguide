import React, { useState } from "react";
import { askQuestion } from "../api";

function ChatScreen({ selectedDocument }) {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setResult(null);

    try {
      const res = await askQuestion(selectedDocument.id, question);
      setResult(res.data);
    } catch (err) {
      setResult({ answer: "Error getting answer. Please try again." });
    }
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h2>Ask a Question</h2>
      <p style={styles.docName}>
        Document: <strong>{selectedDocument.filename}</strong>
      </p>
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask anything about this document..."
        rows={3}
        style={styles.textarea}
      />
      <button onClick={handleAsk} disabled={loading} style={styles.button}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {result && (
        <div style={styles.result}>
          <p>
            <strong>Answer:</strong> {result.answer}
          </p>
          {result.confidence && (
            <p>
              <strong>Confidence:</strong>
              <span
                style={{
                  ...styles.badge,
                  backgroundColor:
                    result.confidence === "high"
                      ? "#28a745"
                      : result.confidence === "medium"
                        ? "#ffc107"
                        : "#dc3545",
                }}
              >
                {result.confidence}
              </span>
            </p>
          )}
          {result.source_pages?.length > 0 && (
            <p>
              <strong>Source Pages:</strong> {result.source_pages.join(", ")}
            </p>
          )}
          {result.reasoning && (
            <p>
              <strong>Reasoning:</strong> {result.reasoning}
            </p>
          )}
        </div>
      )}
    </div>
  );
}

const styles = {
  container: { padding: "20px" },
  docName: { color: "#555" },
  textarea: {
    display: "block",
    width: "400px",
    padding: "8px",
    margin: "10px 0",
  },
  button: {
    padding: "10px 20px",
    cursor: "pointer",
    backgroundColor: "#0066cc",
    color: "white",
    border: "none",
    borderRadius: "4px",
  },
  result: {
    marginTop: "20px",
    padding: "16px",
    backgroundColor: "#f9f9f9",
    borderRadius: "6px",
  },
  badge: {
    marginLeft: "8px",
    padding: "2px 10px",
    borderRadius: "12px",
    color: "white",
    fontSize: "13px",
  },
};

export default ChatScreen;
