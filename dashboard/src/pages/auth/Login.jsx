import { Button, Tooltip } from '@mui/material';
import { ToastContainer, toast } from 'react-toastify';
//? ICONS
import { RiAccountCircleLine, RiLockLine, RiEyeLine, RiEyeOffLine, RiLoader4Fill } from 'react-icons/ri';
//? HOOKS
import { useState, useEffect, useRef } from 'react';
// import { useNavigate } from 'react-router-dom';
// //? REDUX
// import { useDispatch, useSelector } from 'react-redux';
// import { setUser, accessTokenSelector } from '../../redux/reducers/UserSlicer';
// import { setTasas } from '../../redux/reducers/tasasSlicer';
import { notify } from '../../api/scripts/notifications';
// import { axiosRequest } from '../../api/axios';
//? IMG
import LogoSM from '/src/assets/img/logo-sm.svg'

const Login = () => {
	// Dynamic states
	const [showPassword, setShowPassword] = useState(false);
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const [loading, setLoading] = useState(false);
	// //redux States and Hooks
	// const dispatch = useDispatch();
	// const token = useSelector(accessTokenSelector);

	const userRef = useRef();
	const passwordRef = useRef();
	// const navigate = useNavigate();

	useEffect(() => {
		// //! Efecto inicial al cargar el componente
		// if (token != '') {
		// 	navigate('/');
		// } else {
		// 	userRef.current.focus();
		// }
	}, []);

	const HandleSubmit = e => {
		//! conexión asíncrona con Axios para login
		// e.preventDefault();
		// setLoading(true);
		// axiosRequest
		// 	.POST('login/', undefined, { username, password })
		// 	.then(response => {
		// 		dispatch(setUser(response.data));
		// 		//* Hace una petición a las tasas con el token recibido y lo dispatched
		// 		axiosRequest.GET('baremos/tasas/actual/', response.data.token)
		// 			.then(response => dispatch(setTasas(response.data)))

		// 		navigate('/');
		// 	})
		// 	.catch(error => {
		// 		if (!error?.response) {
		// 			notify.ERROR('El servidor no responde, comunicarse al 2434')
		// 		} else {
		// 			notify.ERROR(error.response.data.error);
		// 		}
		// 		passwordRef.current.focus();
		// 		setLoading(false);
		// 	});
	};

	return (
		<>
			<div className='flex items-center justify-center min-h-screen p-4'>
				<div className='theme-primary p-8 rounded-xl shadow-2xl w-auto lg:w-[450px]'>
					<img src={LogoSM} />
					<h1 className='text-3xl text-center uppercase font-bold tracking-[5px] text-white mb-5'>Iniciar Sesión</h1>
					<form className='mb-2' onSubmit={HandleSubmit}>
						<div className='relative mb-4'>
							<RiAccountCircleLine className='iconLogin left-3' />
							<input
								type='text'
								className='inputLogin'
								placeholder='Usuario'
								id='user_id'
								ref={userRef}
								required
								autoComplete='off'
								value={username}
								onChange={e => setUsername(e.target.value)}
							/>
						</div>
						<div className='relative mb-8'>
							<RiLockLine className='iconLogin left-3' />
							<input
								type={showPassword ? 'text' : 'password'}
								className='inputLogin'
								placeholder='Contraseña'
								id='password_id'
								ref={passwordRef}
								required
								value={password}
								onChange={e => setPassword(e.target.value)}
							/>
							{showPassword ? (
								<>
									<Tooltip title='Ocultar Contraseña' placement='right'>
										<div>
											<RiEyeOffLine
												onClick={() => setShowPassword(!showPassword)}
												className='iconLogin right-3 hover:cursor-pointer'
											/>
										</div>
									</Tooltip>
								</>
							) : (
								<>
									<Tooltip title='Mostrar Contraseña' placement='right'>
										<div>
											<RiEyeLine
												onClick={() => setShowPassword(!showPassword)}
												className='iconLogin right-3 hover:cursor-pointer'
											/>
										</div>
									</Tooltip>
								</>
							)}
						</div>
						<div>
							<Button
								type='submit'
								color='primary'
								variant='contained'
								size='large'
								disabled={loading}
								className='w-full text-sm font-bold uppercase rounded-lg btn-primary'
							>
								{loading ? (
									<RiLoader4Fill className='animate-spin h-[1.3rem] text-white' />
								) : (
									'Ingresar'
								)}
							</Button>
						</div>
					</form>
				</div>
			</div>
		</>
	);
};

export default Login;
