import Carnet from '/src/components/Carnet'
import CarnetEjem from '/src/assets/img/Carnet.jpg'

function App() {

  return (
    <>
      <div className='flex'>
        <Carnet />
        <img src={CarnetEjem} alt="Carnet" className="h-[8.3cm] w-[5.5cm] border print-hidden" />
      </div >
    </>
  )
}

export default App
