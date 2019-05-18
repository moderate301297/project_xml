<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Database\QueryException;
use Illuminate\Support\Facades\Auth;
use App\User;
use App\Travel;

class HomeController extends Controller
{
    

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function getAll() {
        $users = User::all();
        // return view('index')->with('travels', $users);
        return $users;
    }

    public function getInformation(Request $request) {

        if ($request->has('url_tour')) {
            $url_tour = $request->url_tour;
        }
        if ($request->has('name_tour')) {
            $name_tour = $request->name_tour;
        }
        if ($request->has('type_tour')) {
            $type_tour = $request->type_tour;
        }
        if ($request->has('cost_tour')) {
            $cost_tour = $request->cost_tour;
        }
        if ($request->has('start_date')) {
            $start_date = $request->start_date;
        }

        $users = User::where('type_tour', '=', $type_tour)->get();
        
        return $users;
    }

     public function duLichTrongNuoc(){
        return view('trongnuoc');
    }

    public function duLichNuocNgoai(){
        return view('ngoainuoc');
    }

    public function getHome(){
        $data['travels'] = Travel::all()->take(4);
        return view('index',$data);
    }

    
}