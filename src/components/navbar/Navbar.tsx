import Container from "@/components/global/Container";
import NavSearch from "./NavSearch";
import {Suspense} from "react";



function Navbar() {
    return (
        <nav className='border-b'>
            <Container className='flex flex-col items-center py-8 gap-4'>
                <Suspense>
                    <NavSearch/>
                </Suspense>

            </Container>
        </nav>
    )
}

export default Navbar;