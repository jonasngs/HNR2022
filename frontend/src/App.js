
import "./App.css";
import axios from "axios";
import { useState } from "react";
import { withStyles, makeStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const StyledTableRow = withStyles((theme) => ({
  root: {
    "&:nth-of-type(odd)": {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);

const useStyles = makeStyles({
  table: {
    minWidth: 700,
  },
});

const App = () => {
  const classes = useStyles();
  const [job, setJob] = useState([]);
  const [search, setSearch] = useState("");

  const getJobData = async (search) => {
    try {
      
      const requestUrl = `"https://tranquil-island-54577.herokuapp.com/search/${search}`;
      console.log("test");
      console.log(requestUrl);
      const data = await axios.get(requestUrl);
      console.log(requestUrl);
      console.log(data.data);
      setJob(data.data);
    } catch (e) {
      console.log(e);
    }
  };



  const handleSubmit = (event) => {
    getJobData(search);
    event.preventDefault();
  }

  return (
    <div className="App">
      <h1>Find your ideal jobs here !</h1>
      <form onSubmit={handleSubmit}>
        <label>
          <input type="text" value={search} onChange={(e) => setSearch(e.target.value)} />
        </label>
        <input type="submit" />
      </form>

      <TableContainer component={Paper}>
        <Table className={classes.table} aria-label="customized table">
          <TableHead>
            <TableRow>
              <StyledTableCell> Company name</StyledTableCell>
              <StyledTableCell> Title </StyledTableCell>
              <StyledTableCell> Link </StyledTableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {job
              .map((job) => {
                return (
                  <StyledTableRow>
                    <StyledTableCell component="th" scope="row">
                      {job.company}
                    </StyledTableCell>
                    <StyledTableCell>
                      {job.title}
                    </StyledTableCell>
                    <StyledTableCell>
                      <a href={job.link}>Click here to apply</a>
                    </StyledTableCell>
                  </StyledTableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default App;