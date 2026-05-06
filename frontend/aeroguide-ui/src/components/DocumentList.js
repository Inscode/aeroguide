import React from "react";

function DocumentList({ documents, onSelect, selectedId }) {
  if (documents.length === 0) return <p>No documents uploaded yet.</p>;

  return (
    <div style={styles.container}>
      <h2>Uploaded Documents</h2>
      {documents.map((doc) => (
        <div
          key={doc.id}
          onClick={() => onSelect(doc)}
          style={{
            ...styles.card,
            backgroundColor: selectedId === doc.id ? "#cce0ff" : "#f5f5f5",
          }}
        >
          <div style={styles.filename}>{doc.filename}</div>
          <p style={styles.meta}>
            {doc.document_type} — {new Date(doc.uploaded_at).toLocaleString()}
          </p>
        </div>
      ))}
    </div>
  );
}

const styles = {
  container: { padding: "20px" },
  card: {
    padding: "12px",
    margin: "8px 0",
    borderRadius: "6px",
    cursor: "pointer",
    overflow: "hidden",
  },
  filename: {
    fontWeight: "bold",
    whiteSpace: "nowrap",
    overflow: "hidden",
    textOverflow: "ellipsis",
  },
  meta: { margin: "4px 0", fontSize: "13px", color: "#555" },
};

export default DocumentList;
