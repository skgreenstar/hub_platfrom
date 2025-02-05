import React from "react";
import FileUpload from "./components/FileUpload";
import FileDownload from "./components/FileDownload";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";

const App: React.FC = () => {
  return (
    <Container maxWidth="sm">
      <Box textAlign="center" mt={5}>
        <Typography variant="h3" gutterBottom>Hub Platform</Typography>
        <FileUpload />
        <FileDownload />
      </Box>
    </Container>
  );
};

export default App;