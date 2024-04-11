

const putPerms = (appName: string, tableName: string): permsType => ({
	VIEW: `${appName}.view_${tableName}`.toLowerCase(),
	CREATE: `${appName}.add_${tableName}`.toLowerCase(),
	UPDATE: `${appName}.change_${tableName}`.toLowerCase(),
	DESTROY: `${appName}.delete_${tableName}`.toLowerCase(),
});

//* Objeto con los permisos almacenados.
export const permisosAPI: appPermissionType = Object.freeze({
	AFILIADO: putPerms('afiliados', 'afiliado'),
	PARENTESCO: putPerms('afiliados', 'parentesco'),
	BAREMO: putPerms('baremos', 'baremo'),
	BENEFICIO: putPerms('baremos', 'beneficio'),
	TASA: putPerms('baremos', 'tasas'),
	ASEGURADORA: putPerms('contratantes', 'aseguradora'),
	CONTRATANTE: putPerms('contratantes', 'contratante'),
	REPRESENTANTE: putPerms('contratantes', 'representante'),
	ESPECIALIDAD: putPerms('medicos', 'especialidad'),
	MEDICO: putPerms('medicos', 'medico'),
	PLAN: putPerms('planes', 'plan'),
	SERVICIO: putPerms('servicios', 'servicio'),
	SEDE: putPerms('vales', 'sede'),
	VALE: putPerms('vales', 'vale'),

	TRATAMIENTO: putPerms('vales', 'tratamiento'),
	FACTURA: putPerms('nomina', 'factura'),
	FINIQUITO: putPerms('nomina', 'honorario'),
});
