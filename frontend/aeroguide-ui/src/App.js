import { useEffect, useState } from "react";
import { getDocuments } from "./api";
import ChatScreen from "./components/ChatScreen";
import DocumentList from "./components/DocumentList";
import UploadScreen from "./components/UploadScreen";

function App() {
  const [documents, setDocuments] = useState([]);
  const [selectedDoc, setSelectedDoc] = useState(null);
  const [tab, setTab] = useState("upload");

  const fetchDocuments = async () => {
    const res = await getDocuments();
    setDocuments(res.data);
  };

  useEffect(() => {
    fetchDocuments();
  }, []);

  return (
    <div style={styles.app}>
      <div style={styles.sidebar}>
        <h1 style={styles.logo}>✈ AeroGuide</h1>
        <button
          style={tab === "upload" ? styles.activeTab : styles.tab}
          onClick={() => setTab("upload")}
        >
          Upload
        </button>
        <button
          style={tab === "documents" ? styles.activeTab : styles.tab}
          onClick={() => setTab("documents")}
        >
          Documents
        </button>
        {selectedDoc && (
          <div style={styles.selectedDoc}>
            <p style={styles.selectedLabel}>Selected:</p>
            <p style={styles.selectedName}>{selectedDoc.filename}</p>
          </div>
        )}
      </div>

      <div style={styles.main}>
        {tab === "upload" && (
          <UploadScreen
            onUploadSuccess={() => {
              fetchDocuments();
              setTab("documents");
            }}
          />
        )}
        {tab === "documents" && (
          <div style={styles.documentsLayout}>
            <div style={styles.leftPanel}>
              <DocumentList
                documents={documents}
                onSelect={(doc) => setSelectedDoc(doc)}
                selectedId={selectedDoc?.id}
              />
            </div>
            <div style={styles.rightPanel}>
              {selectedDoc && <ChatScreen selectedDocument={selectedDoc} />}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  app: {
    display: "flex",
    height: "100vh",
    fontFamily: "Arial, sans-serif",
    overflow: "hidden",
  },
  sidebar: {
    width: "220px",
    backgroundColor: "#001f4d",
    color: "white",
    padding: "20px",
  },
  logo: { fontSize: "20px", marginBottom: "30px" },
  tab: {
    display: "block",
    width: "100%",
    padding: "10px",
    margin: "5px 0",
    backgroundColor: "transparent",
    color: "white",
    border: "1px solid #336699",
    borderRadius: "4px",
    cursor: "pointer",
  },
  activeTab: {
    display: "block",
    width: "100%",
    padding: "10px",
    margin: "5px 0",
    backgroundColor: "#0066cc",
    color: "white",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
  },
  selectedDoc: {
    marginTop: "20px",
    padding: "10px",
    backgroundColor: "#003380",
    borderRadius: "6px",
  },
  selectedLabel: { fontSize: "11px", color: "#99bbff", margin: "0" },
  selectedName: {
    fontSize: "13px",
    margin: "4px 0 0 0",
    wordBreak: "break-word",
  },
  main: { flex: 1, overflowY: "auto", backgroundColor: "#ffffff" },
  documentsLayout: { display: "flex", height: "100%" },
  leftPanel: {
    width: "300px",
    borderRight: "1px solid #e0e0e0",
    overflowY: "auto",
  },
  rightPanel: { flex: 1, overflowY: "auto" },
};

export default App;
