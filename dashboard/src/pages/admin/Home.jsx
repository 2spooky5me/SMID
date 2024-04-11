//? COMPONENTS
import Carnet from '/src/components/Carnet'
import AsyncAutocomplete from '/src/components/customs/AsyncAutocomplete';
import MultiAutocomplete from '/src/components/customs/MultiAutocomplete';

import Button from '@mui/material/Button'
//? ICONS 
import { BiPrinter } from 'react-icons/bi'
//? HO
import { useEffect } from 'react';
//? REDUX
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { accessTokenSelector, refreshTokenSelector, setTokens } from '/src/redux/reducers/UserSlicer';
import { axiosRequest } from '/src/api/axios';

export const Home = () => {

	const navigate = useNavigate();
	//* Redux global States
	const token = useSelector(accessTokenSelector);
	const refresh = useSelector(refreshTokenSelector);
	const dispatch = useDispatch();

	useEffect(() => {
		axiosRequest.VERIFY(token, refresh, dispatch, setTokens, navigate)
	}, []);

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


	return (
		<>
			<div className='flex items-center justify-center min-h-screen gap-12 '>
				<div className='bg-gradient-to-b from-neutral-100 to-neutral-300 rounded-lg h-[32vh] w-[60vh] print:hidden p-5'>
					<h1 className='font-bold text-center text-[23px] text-cyan-600'>GENERAR CARNET</h1>
					<div className='m-5'>
						<AsyncAutocomplete
							id='contratanteId'
							name='contratante'
							label='Doctor'
							urlApi='contratantes/contratante/?'
							ver='name'
						/>
					</div>
					<div className='m-5'>
						<MultiAutocomplete
							id='baremosId'
							name='baremos'
							label='Especialidad'
							placeholder='Añadir'
							urlApi='baremos/baremo/?'
							show='description'
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
				<Carnet />
			</div>
		</>
	);
};

export default Home;
