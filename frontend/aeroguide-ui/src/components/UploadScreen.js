import React, { useState } from "react";
import { uploadDocument } from "../api";

const DOCUMENT_TYPES = [
  { value: "passenger_policy", label: "Passenger Policy" },
  { value: "safety_manual", label: "Safety Manual" },
  { value: "airport_procedure", label: "Airport Procedure" },
  { value: "operational_manual", label: "Operational Manual" },
];

function UploadScreen({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [documentType, setDocumentType] = useState("passenger_policy");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return setMessage("Please select a PDF file.");
    setLoading(true);
    setMessage("");
    try {
      const res = await uploadDocument(file, documentType);
      setMessage(
        `Uploaded successfully. ${res.data.total_chunks} chunks indexed`,
      );
      onUploadSuccess();
    } catch (err) {
      setMessage("Upload failed. Please try again.");
    }

    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h2>Upload Airline Document</h2>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        style={styles.input}
      />
      <select
        value={documentType}
        onChange={(e) => setDocumentType(e.target.value)}
        style={styles.input}
      >
        {DOCUMENT_TYPES.map((t) => (
          <option key={t.value} value={t.value}>
            {t.label}
          </option>
        ))}
      </select>
      <button onClick={handleUpload} disabled={loading} style={styles.button}>
        {loading ? "Uploading..." : "Upload"}
      </button>
      {message && <p style={styles.message}>{message}</p>}
    </div>
  );
}

const styles = {
  container: { padding: "20px" },
  input: { display: "block", margin: "10px 0", padding: "8px", width: "300px" },
  button: {
    padding: "10px 20px",
    cursor: "pointer",
    backgroundColor: "#0066cc",
    color: "white",
    border: "none",
    borderRadius: "4px",
  },
  message: { marginTop: "10px", color: "green" },
};

export default UploadScreen;
