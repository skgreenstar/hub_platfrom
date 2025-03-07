import React, { useState, useEffect } from "react";
import {
  Container,
  TextField,
  Button,
  Box,
  Typography,
  List,
  ListItem,
  ListItemText,
  IconButton,
} from "@mui/material";
import { CloudDownload, UploadFile } from "@mui/icons-material";
import Navbar from "../components/Navbar";
import { uploadFile, downloadFile } from "../services/api";
import axios from "axios";

const API_URL = "http://localhost:8000"; // 백엔드 API 주소

const FileManagement: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [files, setFiles] = useState<string[]>([]); // 📂 파일 목록 저장

  // 🔹 파일 목록 불러오기 (백엔드에서 `/files/list` API 호출)
  const fetchFiles = async () => {
    try {
      const response = await axios.get(`${API_URL}/files/list`);
      setFiles(response.data); // API 응답 데이터를 files 상태에 저장
    } catch (error) {
      console.error("파일 목록을 불러오는 중 오류 발생:", error);
    }
  };

  // ✅ **파일 목록을 컴포넌트 마운트 시 자동으로 불러오기**
  useEffect(() => {
    fetchFiles();
  }, []);

  // 🔹 파일 선택 시 상태 업데이트
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setSelectedFile(e.target.files[0]);
    }
  };

  // 📤 파일 업로드 핸들러
  const handleUpload = async () => {
    if (!selectedFile) {
      alert("업로드할 파일을 선택해주세요.");
      return;
    }
    try {
      await uploadFile(selectedFile);
      alert("파일 업로드 성공!");
      setSelectedFile(null);
      fetchFiles(); // ✅ 업로드 성공 후 파일 목록 새로고침
    } catch (error) {
      console.error("업로드 에러:", error);
      alert("파일 업로드에 실패했습니다.");
    }
  };

  // 📥 개별 파일 다운로드 핸들러
  const handleDownload = async (filename: string) => {
    try {
      await downloadFile(filename);
      alert(`${filename} 다운로드 완료.`);
    } catch (error) {
      console.error("다운로드 에러:", error);
      alert("파일 다운로드에 실패했습니다.");
    }
  };

  return (
    <>
      <Navbar />
      <Container>
        {/* 📤 파일 업로드 영역 */}
        <Box sx={{ mt: 3 }}>
          <Typography variant="h5" gutterBottom>
            파일 업로드
          </Typography>
          <input type="file" onChange={handleFileChange} />
          <Button
            variant="contained"
            color="primary"
            startIcon={<UploadFile />}
            onClick={handleUpload}
            sx={{ mt: 2 }}
          >
            업로드
          </Button>
        </Box>

        {/* 📂 파일 목록 + 개별 다운로드 버튼 */}
        <Box sx={{ mt: 5 }}>
          <Typography variant="h5" gutterBottom>
            파일 목록
          </Typography>
          <List>
            {files.length > 0 ? (
              files.map((filename, index) => (
                <ListItem key={index} divider>
                  <ListItemText primary={filename} />
                  <IconButton color="primary" onClick={() => handleDownload(filename)}>
                    <CloudDownload />
                  </IconButton>
                </ListItem>
              ))
            ) : (
              <Typography color="textSecondary">📂 업로드된 파일이 없습니다.</Typography>
            )}
          </List>
        </Box>
      </Container>
    </>
  );
};

export default FileManagement;
