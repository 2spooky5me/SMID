//? COMPONENTS
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import CircularProgress from '@mui/material/CircularProgress';
import Checkbox from '@mui/material/Checkbox';
//? ICONS
import { MdCheckBoxOutlineBlank, MdOutlineCheckBox } from 'react-icons/md';
//? HOOKS
import { useState, useEffect, lazy, Suspense } from 'react';
import { useNavigate } from 'react-router-dom';
//? REDUX
import { useDispatch, useSelector } from 'react-redux';
import { accessTokenSelector, refreshTokenSelector, setTokens } from '../../redux/reducers/UserSlicer';
import { axiosRequest } from '../../api/axios';

const icon = <MdCheckBoxOutlineBlank fontSize='large' />;
const checkedIcon = <MdOutlineCheckBox fontSize='medium' />;
const TIME_DELAY = 1000;
const PAGE_SIZE = 18;

const MultiAutocomplete = ({
	urlApi = '',
	viewData = [],
	label,
	readOnly = false,
	id = 'autocompleteId',
	show,
	onChange,
	placeholder = '',
}) => {
	//*Hooks
	const navigate = useNavigate();
	//*Redux global States
	const access = useSelector(accessTokenSelector);
	const refresh = useSelector(refreshTokenSelector);
	const dispatch = useDispatch();
	//*Component states
	const [options, setOptions] = useState([]);
	const [inputValue, setInputValue] = useState('');
	const [value, setValue] = useState([]);
	const [timerId, setTimerID] = useState(undefined);
	const [loading, setLoading] = useState(false);

	//* ----------Handling functions

	const handlingRequest = () => {
		//* Función para facilitar los request, retorna una instancia de Axios
		return axiosRequest.GET_WITH_REFRESH(
			urlApi + `search=${inputValue || ''}&page_size=${PAGE_SIZE}`,
			access,
			refresh,
			setTokens,
			dispatch,
			navigate
		);
	};

	const delayedSearch = () => {
		/*
		*Función para hacer la búsqueda con Delay, es decir, 
		*va a realizar la petición de búsqueda al API cuando terminen de escribir
		1.- Se almacena el ID del timer (que lo devuelve el setTimeout)
		2.- el time delay es cuando hará la petición luego del delay.
		3 .- luego de cargar el timeout setea un nuevo TimerID
		4.- siempre que se va a escribir en el input, se reinicia el timeout para que no spam's peticiones
		*/
		if (urlApi) {
			setLoading(true); // Loading
			setOptions([]); // Coloca las opciones en blanco para que no jodan
			clearTimeout(timerId);
			const newTimerId = setTimeout(() => {
				handlingRequest()
					.then(response => setOptions(response.data.results))
					.finally(() => setLoading(false));
			}, TIME_DELAY);
			setTimerID(newTimerId);
		}
	};

	const handlingRenderOptions = (props, option, { selected }) => {
		/*
	* valida si en los valores seleccionados, existe la opción que acaba
		* de recibir del api
		* values incluye (filtro de API.id == seleccionado.id) es un array de 1 elemento [0]
	selected: bool (true || false)
	*/
		selected = value.includes(
			value.filter(value => value.id === option?.id)[0]
		);
		return (
			<li {...props}>
				<Checkbox
					icon={icon}
					checkedIcon={checkedIcon}
					style={{ marginRight: 5 }}
					checked={selected}
				/>
				{option[show]}
			</li>
		);
	};
	const handlingOnChange = (e, value) => {
		setValue(value);
		onChange(value);
	};

	//*--------------------------Use Effect functions
	useEffect(delayedSearch, [inputValue]);
	useEffect(() => {
		/*
	*Recibe los datos desde el padre, para cuando se haga un Retrieve
	en especial para cargar los Baremos :3
	*/
		if (viewData?.length) {
			setValue(viewData);
		} else {
			setValue([])
		}
	}, [viewData]);

	return (
		<>
			<Autocomplete
				multiple
				disableCloseOnSelect
				filterOptions={x => x}
				disabled={readOnly}
				options={options}
				id={id}
				sx={{ width: 'full', maxHeight: '80px' }}
				getOptionLabel={option => option[show]}
				onChange={handlingOnChange}
				isOptionEqualToValue={(option, value) => {
					if (!value?.id) {
						return true
					}
					return value.id === option.id
				}}
				value={value}
				loading={loading}
				renderOption={handlingRenderOptions}
				renderInput={params => (
					<TextField
						{...params}
						label={label}
						placeholder={placeholder}
						value={inputValue}
						onChange={e => setInputValue(e.target.value)}
						InputProps={{
							...params.InputProps,
							endAdornment: (
								<>
									{loading ? (
										<CircularProgress color='inherit' size={20} />
									) : null}
								</>
							),
						}}
					/>
				)}
			/>
		</>
	);
};
export default MultiAutocomplete;
