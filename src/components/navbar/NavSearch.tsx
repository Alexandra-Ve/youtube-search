'use client';
import { Input } from '../ui/input';
import { useSearchParams, useRouter } from 'next/navigation';
import { useDebouncedCallback } from 'use-debounce';
import { useState, useEffect } from 'react';


function NavSearch() {
    const searchParams = useSearchParams();
    // console.log("input searched for: " +  searchParams);
    const {replace} = useRouter();
    const [search, setSearch] = useState(searchParams.get('search')?.toString() || '');
    console.log(search);

    const handleSearch = useDebouncedCallback( (value:string) => {
        const params = new URLSearchParams(searchParams);
        if(value) {
            params.set('search', value)
        } else {
            params.delete('search')
        }
        replace(`/?${params.toString()}`)
    } , 300)


    useEffect(() => {
        if(!searchParams.get('search')){
            setSearch('')
        }
    }, [searchParams.get('search')]);
    return (
        <Input type='search' placeholder='search videos ...' className='max-w-xs'
            onChange={ (e) => {
                    setSearch(e.target.value)
                    handleSearch(e.target.value)
                }
            }
        />
    );
}

export default NavSearch;