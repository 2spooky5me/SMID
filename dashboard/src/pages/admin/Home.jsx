//? COMPONENTS
import Navbar from '/src/components/Navbar';
import Carnet from '/src/components/Carnet'
import AsyncAutocomplete from '/src/components/customs/AsyncAutocomplete';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button'
//? ICONS 
import { BiPrinter } from 'react-icons/bi'
//? HOOKS
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
//? REDUX
import { useSelector, useDispatch } from 'react-redux';
import { refreshTokenSelector, accessTokenSelector, setTokens } from '../../redux/reducers/UserSlicer';
import { axiosRequest } from '../../api/axios';

const initialValues = {
  code: '',
  first_name: '',
  second_name: '',
  last_name: '',
  second_last_name: '',
  identification: '',
  identification_nature: '',
  rif: '',
  rif_nature: '',
  photo: null,
  sex: '',
  specialties: [],
};

export const Home = () => {

  //* GENERAL STATES
  const [values, setValues] = useState(initialValues);
  const [specialty, setSpecialty] = useState([])
  const access = useSelector(accessTokenSelector);
  const refresh = useSelector(refreshTokenSelector);
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handlePrint = () => {
    window.print({
      margins: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0,
      },
      header: "",
      footer: "",
    });
  };


  useEffect(() => {
    // valida que el token siga activo
    axiosRequest.VERIFY(access, refresh, dispatch, setTokens, navigate);
  }, [access, dispatch, navigate, refresh]);

  return (
    <>
      <Navbar />
      <div className='flex items-center justify-center min-h-screen gap-12 print:m-0 print:items-start print:justify-start'>
        <div className='bg-gradient-to-b from-neutral-100 to-neutral-300 rounded-lg h-[38vh] w-[60vh] print:hidden p-5'>
          <h1 className='font-bold text-center text-[23px] text-cyan-600'>GENERAR CARNET</h1>
          <div className='m-5'>
            <AsyncAutocomplete
              id='doctorInfo'
              name='doctor'
              label='Doctor'
              values={values.doctor_name}
              disabled={values.specialties.length == 0 ? true : false}
              onChange={(e, newVal) => {
                setSpecialty([]); // limpia el estado de specialty
                setValues(values => ({ ...values, specialties: [] })); // limpia el campo specialties en values
                setValues(value => ({ ...value, ...newVal }));
              }}
              urlApi='medicos/medico/?'
              ver='full_name'
            />
          </div>
          <div className='m-5'>
            <Autocomplete
              multiple
              id="tags-outlined"
              options={values.specialties}
              getOptionLabel={(option) => option.name}
              disabled={values.specialties.length == 0 ? true : false}
              filterSelectedOptions
              onChange={(event, newValue) => {
                if (newValue.length <= 2) {
                  setSpecialty(newValue);
                }
              }}
              value={specialty}
              renderInput={(params) => (
                <TextField
                  {...params}
                  label="Seleccionar Especialidad"
                  placeholder="Especialidades"
                />
              )}
            />
          </div>
          <div className='m-5'>
            <Button
              onClick={handlePrint}
              variant='contained'
              color='primary'
              className='w-full'
              startIcon={<BiPrinter />}>
              Imprimir
            </Button>
          </div>
        </div>
        <Carnet
          doctor={values}
          specialty={specialty}
        />
      </div>
    </>
  );
};

export default Home;
