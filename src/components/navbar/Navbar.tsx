import Container from "@/components/global/Container";
import NavSearch from "./NavSearch";


function Navbar() {
    return (
        <nav className='border-b'>
            <Container className='flex flex-col items-center py-8 gap-4'>
                <NavSearch/>
            </Container>
        </nav>
    )
}

export default Navbar;