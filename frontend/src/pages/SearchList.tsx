import React, { useState } from "react";
import { Container, TextField, Button, List, ListItem, ListItemText, Box } from "@mui/material";
import { fetchDocuments } from "../services/api";
import Navbar from "../components/Navbar";

const SearchList = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const data = await fetchDocuments(query);
      setResults(data);
    } catch (error) {
      alert("검색 실패");
    }
  };

  return (
    <>
      <Navbar />
      <Container>
        <Box sx={{ mt: 3 }}>
          <TextField label="검색어 입력" variant="outlined" fullWidth value={query} onChange={(e) => setQuery(e.target.value)} />
          <Button variant="contained" color="primary" fullWidth onClick={handleSearch} sx={{ mt: 2 }}>
            검색
          </Button>
        </Box>
        <List sx={{ mt: 3 }}>
          {results.map((doc, index) => (
            <ListItem key={index} divider>
              <ListItemText primary={doc.title} secondary={doc.description} />
            </ListItem>
          ))}
        </List>
      </Container>
    </>
  );
};

export default SearchList;
