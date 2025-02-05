import React, { useState } from "react";
import { uploadFile } from "../services/api";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";

const FileUpload = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleUpload = async () => {
    if (!file) {
      alert("파일을 선택해주세요!");
      return;
    }

    try {
      await uploadFile(file);
      alert("파일 업로드 성공");
    } catch (error) {
      alert("파일 업로드 실패! 네트워크 상태를 확인하세요.");
      console.error("Upload Error:", error);
    }
  };

  return (
    <Stack spacing={2} alignItems="center">
      <input 
        type="file" 
        onChange={(e) => setFile(e.target.files?.[0] || null)} 
        style={{ display: "block", padding: "10px" }}
      />
      <Button variant="contained" color="primary" onClick={handleUpload}>
        업로드
      </Button>
    </Stack>
  );
};

export default FileUpload;
