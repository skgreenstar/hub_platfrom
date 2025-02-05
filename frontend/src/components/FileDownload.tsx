import React, { useState } from "react";
import { downloadFile } from "../services/api";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Stack from "@mui/material/Stack";

const FileDownload = () => {
  const [filename, setFilename] = useState("");

  const handleDownload = async () => {
    if (!filename) {
      alert("다운로드할 파일명을 입력하세요.");
      return;
    }
    await downloadFile(filename);
  };

  return (
    <Stack spacing={2} alignItems="center">
      <TextField 
        label="파일명 입력"
        variant="outlined"
        value={filename}
        onChange={(e) => setFilename(e.target.value)}
      />
      <Button variant="contained" color="secondary" onClick={handleDownload}>
        다운로드
      </Button>
    </Stack>
  );
};

export default FileDownload;