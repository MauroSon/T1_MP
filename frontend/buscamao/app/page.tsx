import Footer from "./components/Footer";
import Navbar from "./components/NavBar";
import { FiltroComponent } from "./components/FiltroComponent";
export default function Home() {
  return (
    <div>
      <Navbar></Navbar>
      <div className="ml-5 mr-2 my-8">
      <FiltroComponent/>

      </div>
      teste
      <Footer></Footer>
    </div>
  );
}