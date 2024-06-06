import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Paper from '@mui/material/Paper';

function Formulario(props){
    return (
        <Paper elevation={3} sx={{m:2}}>
<Grid container sx={{p:2}} spacing={1}>
  <Grid item xs={12}>
    <h3>
      {props.titulo}
    </h3>                
  </Grid>  
  <Grid item xs={12}>
    <TextField fullWidth label='Nome' />            
  </Grid>    
  <Grid item xs={6}>
    <TextField fullWidth type='' label='Telefone' />            
  </Grid> 
  <Grid item xs={6}>
    <TextField fullWidth label='Whatsapp' />            
  </Grid>               
  <Grid item xs={6}>
    <TextField fullWidth label='E-mail' />            
  </Grid> 
  <Grid item xs={6}>
    <TextField fullWidth type={'date'} label='Data de nascimento' />            
  </Grid>      
  <Grid item xs={6}>
    <Button variant='contained' fullWidth color='error'>Cancelar</Button>           
  </Grid> 
  <Grid item xs={6}>
    <Button variant='contained' fullWidth>Salvar</Button>           
  </Grid>                                                                                
</Grid>
        </Paper>        
    );
}

Formulario.propTypes = {
    titulo : PropTypes.string,
  }
  
export default Formulario;