//? COMPONENTS
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
    rif: '',
    identification: '',
    first_name: '',
    last_name: '',
    photo: '',
    specialtys: [],
    selected_specialty: ''
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
            <div className='flex items-center justify-center min-h-screen gap-12 print:m-0 print:items-start print:justify-start'>
                <div className='bg-gradient-to-b from-neutral-100 to-neutral-300 rounded-lg h-[38vh] w-[60vh] print:hidden p-5'>
                    <h1 className='font-bold text-center text-[23px] text-cyan-600'>GENERAR CARNET</h1>
                    <div className='m-5'>
                        <AsyncAutocomplete
                            id='doctorInfo'
                            name='doctor'
                            label='Doctor'
                            values={values.doctor_name}
                            onChange={
                                (e, newVal) => {
                                    if (newVal != null) {
                                        setValues(Val => ({
                                            ...Val,
                                            code: newVal.code,
                                            identification: newVal.identification,
                                            identification_nature: newVal.identification_nature,
                                            rif: newVal.rif,
                                            identification_rif: newVal.identification_rif,
                                            first_name: newVal.first_name,
                                            last_name: newVal.last_name,
                                            photo: newVal.photo,
                                            specialtys: newVal.specialty
                                        }))
                                    } else {
                                        setValues(initialValues)
                                    }
                                }
                            }
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
                            disabled={values.specialtys.length == 0 ? true : false}
                            options={values.specialtys}
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
                    doctor_info={values}
                />
            </div>
        </>
    );
};

export default Home;
