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

        if ($request->has('type_tour')) {
            $type_tour = $request->type_tour;
        }

        if ($request->has('name_tour')) {
            $name_tour = "%".$request->name_tour."%";
            // $users = User::where('type_tour', '=', $type_tour)
            // ->where('name_tour', 'LIKE', $name_tour)
            // ->get();
            // return $users;
        } 

        if ($request->has('number_date')) {
            $number_date = $request->number_date;
            $users = User::where('type_tour', '=', $type_tour)
            ->where('number_date', '=', $number_date)
            ->get();
            return $users;
        }

        if ($request->has('start_date')) {
            $start_date = "%" .$request->start_date ."%";
        }
         
        if ($request->has('cost_tour')) {
            $cost_tour = $request->cost_tour;

            if ($cost_tour == '[]') {
                $cost_tour_start = 0;
                $cost_tour_end = 100000000;
            } else {
                $cost_tour_start = $cost_tour[0];
                $cost_tour_end = $cost_tour[1];
            }

            $users = User::where('type_tour', '=', $type_tour)
            ->where('cost_tour', '>=', $cost_tour_start)
            ->where('cost_tour', '<=', $cost_tour_end)
            ->get();
            return $users;
        }
        
        if ($request->has('start_date')) {
            $start_date = "%" .$request->start_date ."%";
        }

        $users = User::where('type_tour', '=', $type_tour)
            ->where('name_tour', 'LIKE', $name_tour)
            ->where('cost_tour', '>=', $cost_tour_start)
            ->where('cost_tour', '<=', $cost_tour_end)
            ->where('start_date', 'LIKE', $start_date)
            ->get();
        
        return $users;
    }

     public function duLichTrongNuoc(){
        return view('trongnuoc');
    }

    public function duLichNuocNgoai(){
        return view('ngoainuoc');
    }

    public function getHome(){
        $data['travels'] = User::all()->take(4);
        return view('index',$data);
    }
    
}