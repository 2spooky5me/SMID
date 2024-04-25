/* eslint-disable react/prop-types */
import CPV from '/src/assets/img/logo-cpv.svg'
import SM from '/src/assets/img/logo-sm.svg'
import DR from '/src/assets/img/default.png'

const Carnet = ({ doctor, specialty }) => {
  console.log(specialty);
  return (
    <>
      <div className='h-[8.3cm] w-[5.5cm] bg-white print-view'>
        <div className='bg-header-carnet h-[1.42cm] flex justify-between p-0'>
          <img src={CPV} alt="Logo Cpv" className='h-[55px]' />
          <img src={SM} alt="Logo Sociedad Medica" className='h-[55px]' />
        </div>
        <div className='fondo-login h-[4.39cm] text-center pt-[1px]'>
          <p className='text-[10px] uppercase text-orangecpv-500 font-bold tracking-wide leading-tight opacity-100'>Centro PoliclÍnico Valencia<br></br>&quot;La Viña&quot;</p>
          <p className='uppercase text-[7px] font-bold text-cyancpv-500'>rif: j-07505586-1</p>
          <div className='flex justify-center mb-1'>
            <img src={doctor?.photo ? doctor?.photo : DR} alt='Doctor' className=' h-[2.8cm] w-[2.5cm] border-2 border-orangecpv-500' />
          </div>
          {doctor?.first_name ?
            (<p className=' text-[13px] font-black capitalize'>{doctor?.sex === 'F' ? 'Dra.' : 'Dr.'} {doctor?.first_name} {doctor?.last_name}</p>)
            : (<></>)}
        </div>
        <div className='bg-cyancpv-500 h-[1.20cm] text-center flex items-center justify-center'>
          <p className='inline-block font-black text-white align-middle text-[13px] uppercase'>
            {specialty.map((item) => (
              <p key={item.id}>{item.name}</p>
            ))}
          </p>
        </div>
        <div className='h-[0.37cm] border-b-[1.5px] border-cyancpv-500 text-[10px] font-bold flex justify-between'>
          <p className='ml-2'>RIF: {doctor?.rif_nature}-{doctor?.rif}</p> <p className='mr-2'>C.I.: {doctor?.identification_nature}-{doctor?.identification}</p>
        </div>
        <div className='h-[0.92cm] flex justify-between uppercase border-b-[1.5px] border-cyancpv-500 font-bold'>
          <div className='leading-[9px] text-cyancpv-500 text-[8px] mt-1 ml-2'>
            <p>Asociación civil de la </p>
            <p className='font-extrabold text-[10px]'>sociedad médica</p>
            <p>rif: j-12345678-9</p>
          </div>
          <div className='text-orangecpv-500 text-[7px] mr-2 mt-1 leading-[9px] text-center'>
            <p>código:</p>
            <p className='font-bold text-[12px] mt-1'>{doctor?.code}</p>
          </div>

        </div>
      </div>
    </>
  )
}

export default Carnet