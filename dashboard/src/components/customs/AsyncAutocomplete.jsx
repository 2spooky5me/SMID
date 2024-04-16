//? COMPONENTES
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import CircularProgress from '@mui/material/CircularProgress';
//? HOOKS
import { useNavigate } from 'react-router-dom';
import { useState, useEffect} from 'react';
//? REDUX
import { axiosRequest } from '/src/api/axios';
import { useDispatch, useSelector } from 'react-redux';
import { accessTokenSelector, refreshTokenSelector, setTokens } from '/src/redux/reducers/UserSlicer';

const AsyncAutocomplete = ({
	urlApi = '',
	ver,
	readOnly,
	id,
	onChange,
	value,
	label,
	children,
	filterOpts,
	disableClearable,
	add
}) => {
    
    //*HOOKS
	const navigate = useNavigate();
	//*REDUX
	const dispatch = useDispatch();
	const access = useSelector(accessTokenSelector);
	const refresh = useSelector(refreshTokenSelector);
	//*GENERALS STATES
	const [data, setData] = useState([]);
	const [open, setOpen] = useState(false);
	const [loading, setLoading] = useState(false);

	const [inputValue, setInputValue] = useState('');
	const [timerId, setTimerID] = useState(undefined);
	const WAIT_INTERVAL = 1000;


	const searchOptions = async val => {

		axiosRequest
			.GET(
				urlApi + `search=${val || ''}`,
				access,
                refresh,
				setTokens,
				dispatch,
				navigate
			)
			.then(response => {
				//* por ahora si se añade una opcion a traves del parametro add a los datos
				//* no aparece en la busqueda
				// setData(add ? [...response.data.results, ...add] : response.data.results || response.data.beneficios);
                setData(response.data)
			})
			.finally(() => setLoading(false))
	};

	const prevFilterChange = () => {
		if (filterOpts && filterOpts[0]) {
			setInputValue('');
		}
	}

	useEffect(prevFilterChange, [filterOpts && (filterOpts[0])])

	const delayedSearch = () => {
		//* Función para que pueda realizar la búsqueda en el autocomplete cuando terminen de escribir
		//*	para que no busque en el API con cada tecla presionada, sino al terminar de escribir

		if (urlApi) {
			setData([])
			setLoading(true);
			clearTimeout(timerId);
			const newTimerId = setTimeout(() => {
				searchOptions(filterOpts && (`${filterOpts[0]}+${inputValue}`) || inputValue);
			}, WAIT_INTERVAL);
			setTimerID(newTimerId);
		}
	};

	//* ----------------------------- useEffect Functions --------------------------------------
	useEffect(delayedSearch, [inputValue, urlApi, filterOpts && filterOpts[0]])

	return (
		<>
			<Autocomplete
				disabled={readOnly}
				disableClearable={disableClearable}
				id={id}
				sx={{ width: 'full' }}
				color='primary'
				open={open}
				onOpen={() => setOpen(true)}
				onClose={() => setOpen(false)}
				getOptionLabel={option => option[ver] || ''}
				isOptionEqualToValue={(option, value) => {
					if (!value?.id) {
						return true
					}
					return option.id === value.id
				}}
				autoHighlight
				value={value}
				onChange={(evt, value, reason, details) => onChange(evt, value, reason, details)}
				loading={loading}
				options={data}
				filterOptions={(options, state) => {
					//* Filtro opcional el cual retorna una lista de elementos filtrados
					//* basado en el codigo escrito en string del index 1 del prop filterOpts
					const filteredOpts = filterOpts && (
						eval(filterOpts[1])
					);

					// Lista de llaves y fields
					const results = (filteredOpts || options).filter((value) => {

						//* Filter para que busque iterando cada diccionario del array
						return Object.keys(value).some((field) => {
							/*
							*1.- function filter sobre la lista de resultados del autocomplete
							* 2.- Object.keys() para tener un array de los campos y fields
							*   3.- Al array de Keys aplica some() el cual al momento de devolver true
							?			detendrá la iteración. (recordar que el filter itera tantas veces resultados haya)
							*			4.- si value(options).field(keyList) es string
							!retornara true si el inputValue tiene un texto que pueda hacer match con cualquiera
							!de los valores de algún campo, por ejemplo si se busca por cédula, o ficha,
							!encontrara a los resultados
							*/
							const val = value[field]
							if (typeof val === 'string') {
								return val.toLowerCase().includes(state.inputValue.toLowerCase())
							} else return false
						})
					})
					return results
				}}
				renderInput={params => (
					<TextField
						fullWidth
						{...params}
						label={label}
						value={inputValue}
						onChange={e => setInputValue(e.target.value)}
						InputProps={{
							...params.InputProps,
							endAdornment: (
								<>
									{loading ? (
										<CircularProgress color='inherit' size={20} />
									) : null}
									{params.InputProps.endAdornment}
									{children}
								</>
							),
						}}
					/>
				)}
			/>
		</>
	);
};

export default AsyncAutocomplete;
