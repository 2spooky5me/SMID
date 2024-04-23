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
                            onChange={(e,newVal) => {
                                setValues(value => ({ ...value,...newVal }));
                            }}
                            urlApi='medicos/medico/?'
                            ver='full_name'
                        />
                    </div>
                    <div className='m-5'>
                        <Autocomplete
                            id='especialidadMedico'
                            name='especialidad'
                            label='Especialidad'
                            value={values.selected_specialty || ''}
                            disabled={values.specialties.length == 0 ? true : false}
                            options={values.specialties}
                            getOptionLabel={(option) => option.name ?? option}
                            renderInput={(params) => <TextField {...params} label="Especialidad" />}
                            onChange={
                                (e, newVal) => {
                                    if (newVal != null) {
                                        setValues(Val => ({
                                            ...Val,
                                            selected_specialty: newVal.name
                                        }))
                                    } else {
                                        setValues(Val => ({
                                            ...Val,
                                            selected_specialty: ''
                                        }))
                                    }
                                }
                            }
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
                />
            </div>
        </>
    );
};

export default Home;
