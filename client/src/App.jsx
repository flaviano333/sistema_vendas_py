import './App.css'
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Divider from '@mui/material/Divider';
import Paper from '@mui/material/Paper';
import Formulario from './componentes/Formulario';
import PropTypes from 'prop-types';

function App() {
  return (
      <Grid container>
        <Grid item xs={2}>
        </Grid>
        <Grid item xs={10}>
          <Formulario titulo = 'Meu formulário' />
          <Formulario titulo = 'Meu segundo formulário' />
          <Formulario titulo = 'Meu terceiro formulário' />          
        </Grid>                      
      </Grid>
  );
}

export default App
