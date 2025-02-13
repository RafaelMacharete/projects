import './Header.css'

export default function Header() {
    return (
        <>
            <header>
                <nav>
                    <h1 className='text-red-400'>Rafael Macharete</h1>
                    <ul>
                        <li><a href="#"><span>#home</span></a></li>
                        <li><a href="#"><span>#works</span></a></li>
                        <li><a href="#"><span>#about-me</span></a></li>
                        <li><a href="#"><span>#contacts</span></a></li>
                    </ul>
                </nav>
            </header>
        </>
    )
}