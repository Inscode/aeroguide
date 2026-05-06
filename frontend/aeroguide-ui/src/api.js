import axios from "axios"

const BASE_URL = 'http://localhost:8000';

export const uploadDocument = async (file, documentType) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('document_type', documentType);
    return await axios.post(`${BASE_URL}/documents/upload`, formData);
}

export const getDocuments = async () => {
    return  await axios.get(`${BASE_URL}/documents`);
}

export const askQuestion = async (documentId, question) => {
    return  await axios.post(`${BASE_URL}/query/ask`, {
        document_id: documentId,
        question: question
    })
};